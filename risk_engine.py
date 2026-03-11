from security_checks import check_https, check_domain_age, suspicious_keywords, long_url

def analyze_url(url):

    score = 100
    reasons = []

    if not check_https(url):
        score -= 30
        reasons.append("Website does not use HTTPS")

    if suspicious_keywords(url):
        score -= 20
        reasons.append("URL contains suspicious keywords")

    if long_url(url):
        score -= 10
        reasons.append("URL is unusually long")

    if not check_domain_age(url):
        score -= 10
        reasons.append("Domain age could not be verified")

    return score, reasons