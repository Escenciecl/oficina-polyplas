#!/usr/bin/env python3
"""
Agente Medición — revisión automática de experimentos.
Lee tasks/experimentos.json, compara métricas post-cambio vs pre-cambio en GSC,
y actualiza el estado (mejoro / degrado / igual).

Requiere: GSC_CREDENTIALS env var con JSON de service account.
"""
import json, os, sys
from datetime import date, timedelta

try:
    from googleapiclient.discovery import build
    from google.oauth2 import service_account
except ImportError:
    print("Instala: pip install google-api-python-client google-auth", file=sys.stderr)
    sys.exit(1)

SITE = 'sc-domain:polyplas.cl'
TODAY = date.today()
MIN_DAYS_DATA = 7  # mínimo de días con datos antes de revisar
CTR_THRESHOLD = 0.002   # +/- 0.2 pp para considerar cambio
CLICKS_THRESHOLD = 10   # mínimo de clics post para resultado válido


def get_gsc_service():
    creds_json = os.environ.get('GSC_CREDENTIALS')
    if not creds_json:
        print("ERROR: GSC_CREDENTIALS no configurado", file=sys.stderr)
        return None
    info = json.loads(creds_json)
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=['https://www.googleapis.com/auth/webmasters.readonly']
    )
    return build('searchconsole', 'v1', credentials=creds)


def get_gsc_metrics(service, url, start_date, end_date):
    """Obtiene clics, impresiones, CTR y posición para una URL en un período."""
    try:
        result = service.searchanalytics().query(
            siteUrl=SITE,
            body={
                'startDate': start_date.isoformat(),
                'endDate': end_date.isoformat(),
                'dimensions': ['page'],
                'dimensionFilterGroups': [{
                    'filters': [{'dimension': 'page', 'expression': url}]
                }],
                'rowLimit': 1
            }
        ).execute()
    except Exception as e:
        print(f"  Error GSC para {url}: {e}", file=sys.stderr)
        return None

    rows = result.get('rows', [])
    if not rows:
        return None

    r = rows[0]
    return {
        'clicks': int(r.get('clicks', 0)),
        'impressions': int(r.get('impressions', 0)),
        'ctr': round(r.get('ctr', 0), 4),
        'position': round(r.get('position', 0), 1)
    }


def evaluate_gsc_result(current, pre, baseline_ctr):
    """Compara métricas post-cambio con pre-cambio y determina resultado."""
    if current is None:
        return 'revision_pendiente', {}, 'Sin datos GSC en el período post-cambio'

    if current['clicks'] < CLICKS_THRESHOLD:
        return 'revision_pendiente', current, f"Solo {current['clicks']} clics — pocos datos para concluir"

    # Referencia: período pre-cambio (preferido) o baseline histórico
    ref_ctr = pre['ctr'] if pre else baseline_ctr
    ref_clicks = pre['clicks'] if pre else 0

    delta_abs = current['ctr'] - ref_ctr
    delta_rel = (delta_abs / ref_ctr * 100) if ref_ctr > 0 else 0

    if delta_abs > CTR_THRESHOLD:
        estado = 'mejoro'
    elif delta_abs < -CTR_THRESHOLD:
        estado = 'degrado'
    else:
        estado = 'igual'

    delta = {
        'ctr_pre': ref_ctr,
        'ctr_post': current['ctr'],
        'delta_abs': round(delta_abs, 4),
        'delta_rel_pct': round(delta_rel, 1),
        'clics_pre': ref_clicks,
        'clics_post': current['clicks'],
        'impresiones_post': current['impressions'],
        'posicion_post': current['position']
    }

    return estado, delta, None


def process_experiment(service, exp):
    """Procesa un experimento y retorna si fue actualizado."""
    print(f"\n[{exp['id']}] {exp['cambio']}")

    aplicado = date.fromisoformat(exp['aplicado'])
    revisar = date.fromisoformat(exp['revisar_en'])

    if TODAY < revisar:
        dias = (revisar - TODAY).days
        print(f"  → No es momento de revisar. Faltan {dias} día(s) ({exp['revisar_en']})")
        return False

    url = exp['url_muestra']
    metrica = exp.get('metrica_primaria', {})

    # Período post-cambio: desde aplicado+1 hasta hoy (máx 28 días)
    post_start = aplicado + timedelta(days=1)
    post_end = min(TODAY, aplicado + timedelta(days=28))

    # Período pre-cambio: misma duración, antes del cambio
    window = (post_end - post_start).days
    pre_end = aplicado - timedelta(days=1)
    pre_start = pre_end - timedelta(days=window)

    print(f"  URL: {url}")
    print(f"  Post-cambio: {post_start} → {post_end} ({window}d)")
    print(f"  Pre-cambio:  {pre_start} → {pre_end} ({window}d)")

    if metrica.get('tipo') == 'gsc':
        current = get_gsc_metrics(service, url, post_start, post_end)
        pre = get_gsc_metrics(service, url, pre_start, pre_end)

        baseline_ctr = exp.get('baseline', {}).get('metricas', {}).get('ctr', 0)
        estado, delta, nota = evaluate_gsc_result(current, pre, baseline_ctr)

        revision = {
            'fecha': TODAY.isoformat(),
            'metricas': current,
            'metricas_pre': pre,
            'delta': delta,
            'ventana_post': f"{post_start} → {post_end}",
            'ventana_pre': f"{pre_start} → {pre_end}"
        }
        if nota:
            revision['nota'] = nota

        exp['estado'] = estado
        exp['revisiones'].append(revision)

        if nota:
            print(f"  → {estado}: {nota}")
        elif delta:
            d = delta
            pre_pct = f"{d.get('ctr_pre', 0)*100:.1f}%"
            post_pct = f"{d.get('ctr_post', 0)*100:.1f}%"
            dpp = f"{d.get('delta_abs', 0)*100:+.1f} pp"
            drel = f"{d.get('delta_rel_pct', 0):+.1f}%"
            print(f"  → {estado}: CTR {pre_pct} → {post_pct} ({dpp} · {drel}) | Clics: {d.get('clics_pre',0)} → {d.get('clics_post',0)}")

        return True

    elif metrica.get('tipo') == 'pagespeed':
        # PageSpeed metrics se capturan con Lighthouse — marcar para revisión manual
        exp['estado'] = 'revision_pendiente'
        exp['revisiones'].append({
            'fecha': TODAY.isoformat(),
            'nota': 'Revisión PageSpeed pendiente — ejecutar Lighthouse manualmente'
        })
        print(f"  → revision_pendiente (PageSpeed requiere Lighthouse manual)")
        return True

    return False


def main():
    service = get_gsc_service()
    if not service:
        sys.exit(1)

    exp_path = os.path.join(os.path.dirname(__file__), '..', 'tasks', 'experimentos.json')
    exp_path = os.path.normpath(exp_path)

    with open(exp_path, encoding='utf-8') as f:
        experiments = json.load(f)

    updated = False
    for exp in experiments:
        if exp['estado'] not in ('pendiente', 'revision_pendiente'):
            print(f"[{exp['id']}] Estado '{exp['estado']}' — sin acción")
            continue
        if process_experiment(service, exp):
            updated = True

    if updated:
        with open(exp_path, 'w', encoding='utf-8') as f:
            json.dump(experiments, f, ensure_ascii=False, indent=2)
        print("\n✓ experimentos.json actualizado")
    else:
        print("\nSin cambios en experimentos.json")

    # Resumen para el log
    mejoron = sum(1 for e in experiments if e['estado'] == 'mejoro')
    degrado = sum(1 for e in experiments if e['estado'] == 'degrado')
    pendientes = sum(1 for e in experiments if e['estado'] == 'pendiente')
    print(f"\nResumen: {mejoron} mejoraron · {degrado} degradaron · {pendientes} en curso")


if __name__ == '__main__':
    main()
