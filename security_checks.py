import requests
from urllib.parse import urlparse

def check_https(url):
    try:
        response = requests.get("https://" + url, timeout=5)
        if response.url.startswith("https"):
            return True
    except:
        return False

def check_domain_age(url):
    # simple placeholder check
    if len(url) < 5:
        return False
    return True

def suspicious_keywords(url):
    bad_words = ["login", "verify", "update", "bank"]
    for word in bad_words:
        if word in url.lower():
            return True
    return False

def long_url(url):
    if len(url) > 50:
        return True
    return False