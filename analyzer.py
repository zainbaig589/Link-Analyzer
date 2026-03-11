from risk_engine import analyze_url


def get_analysis(url):

    score, reasons = analyze_url(url)

    if score >= 40:

        verdict = "Website Looks Safe"

    else:

        verdict = "Potentially Risky Website"

    return score, verdict, reasons