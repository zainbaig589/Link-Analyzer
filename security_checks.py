import socket
import ssl
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime


def clean_domain(url):
    url = url.replace("http://", "").replace("https://", "")
    return url.split("/")[0]


# -----------------------------
# HTTPS TLS HANDSHAKE CHECK
# -----------------------------

def check_https(domain):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return cert

    except:
        return None


# -----------------------------
# SSL EXPIRY CHECK
# -----------------------------

def check_ssl_expiry(cert):

    try:
        expiry = cert['notAfter']
        expiry_date = datetime.strptime(expiry, "%b %d %H:%M:%S %Y %Z")

        if expiry_date < datetime.utcnow():
            return False, expiry_date
        else:
            return True, expiry_date

    except:
        return False, None


# -----------------------------
# HTTPS REDIRECT CHECK
# -----------------------------

def check_https_redirect(domain):

    try:
        url = "http://" + domain
        response = requests.get(url, timeout=5, allow_redirects=True)

        if response.url.startswith("https"):
            return True

        return False

    except:
        return False


# -----------------------------
# URL LENGTH CHECK
# -----------------------------

def check_url_length(url):

    if len(url) > 75:
        return True

    return False


# -----------------------------
# SUSPICIOUS TLD CHECK
# -----------------------------

def suspicious_tld(domain):

    bad_tlds = [
        ".tk", ".xyz", ".top", ".club",
        ".gq", ".ml", ".ga"
    ]

    for tld in bad_tlds:
        if domain.endswith(tld):
            return True

    return False


# -----------------------------
# DOMAIN AGE CHECK
# -----------------------------

def check_domain_age(domain):

    try:
        info = whois.whois(domain)

        creation = info.creation_date

        if isinstance(creation, list):
            creation = creation[0]

        age = (datetime.now() - creation).days

        return age

    except:
        return None