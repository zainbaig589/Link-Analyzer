from security_checks import *

def analyze_url(url):

    reasons = []
    score = 0

    domain = clean_domain(url)

    # HTTPS check
    cert = check_https(domain)

    if cert:
        score += 20
        reasons.append("HTTPS supported")

        valid, expiry = check_ssl_expiry(cert)

        if valid:
            score += 10
            reasons.append("SSL certificate valid")

        else:
            reasons.append("SSL certificate expired")

    else:
        reasons.append("No HTTPS support")


    # HTTPS redirect
    if check_https_redirect(domain):
        score += 10
        reasons.append("HTTP redirects to HTTPS")

    else:
        reasons.append("No HTTPS redirect")


    # URL length
    if check_url_length(url):
        reasons.append("Suspicious long URL")
        score -= 10


    # TLD
    if suspicious_tld(domain):
        reasons.append("Suspicious domain extension")
        score -= 10


    # Domain age
    age = check_domain_age(domain)

    if age:

        if age > 365:
            score += 20
            reasons.append("Domain older than 1 year")

        else:
            reasons.append("New domain (possible phishing)")
            score -= 10


    return score, reasons