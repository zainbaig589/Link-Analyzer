from risk_engine import analyze_url

def get_analysis(url):

    score, reasons = analyze_url(url)

    if score > 70:
        verdict = "Website Looks Safe"
    elif score > 40:
        verdict = "Website Might Be Suspicious"
    else:
        verdict = "High Risk Website"

    return score, verdict, reasons