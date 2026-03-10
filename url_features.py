import tldextract
import whois
import requests

def url_length(url):
    return len(url)



def has_https(url):
    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith("https"):
            return 1
        else:
            return 0
    except:
        return 0

def suspicious_words(url):
    words = ["login","verify","secure","account","update","bank"]
    for w in words:
        if w in url.lower():
            return 1
    return 0

def domain_age(url):
    try:
        domain = tldextract.extract(url).domain + "." + tldextract.extract(url).suffix
        w = whois.whois(domain)
        if w.creation_date:
            return 1
    except:
        return 0