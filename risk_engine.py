from url_features import *

def calculate_risk(url):

    score = 0
    reasons = []

    if url_length(url) > 50:
        score += 20
        reasons.append("URL is unusually long")

    if has_https(url) == 0:
        score += 30
        reasons.append("Website does not use HTTPS")

    if suspicious_words(url) == 1:
        score += 25
        reasons.append("Suspicious keyword detected")

    if domain_age(url) == 0:
        score += 25
        reasons.append("Domain age unknown or very new")

    return score, reasons