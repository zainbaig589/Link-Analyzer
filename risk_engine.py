from security_checks import *


def analyze_url(url):

    domain = clean_domain(url)

    score = 0
    reasons = []

    cert = check_https(domain)

    if cert:

        score += 20
        reasons.append("HTTPS supported")

        if check_ssl_expiry(cert):

            score += 10
            reasons.append("SSL certificate valid")

        else:
            reasons.append("SSL certificate expired")

    else:

        reasons.append("No HTTPS support")


    if check_https_redirect(domain):

        score += 10
        reasons.append("HTTP redirects to HTTPS")

    else:

        reasons.append("No HTTPS redirect")


    if suspicious_tld(domain):

        score -= 10
        reasons.append("Suspicious domain extension")


    if long_url(url):

        score -= 10
        reasons.append("URL length suspicious")


    age = domain_age(domain)

    if age:

        if age > 365:

            score += 20
            reasons.append("Domain older than 1 year")

        else:

            score -= 10
            reasons.append("New domain")


    return score, reasons