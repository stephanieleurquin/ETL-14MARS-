import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def scan_site(url):
    if url in visited:
        return

    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
        print("Scan:", url)

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])

            # seulement les liens du même domaine
            if urlparse(full_url).netloc == urlparse(url).netloc:
                scan_site(full_url)

    except Exception as e:
        print("Erreur:", e)

start_url = "https://example.com"
scan_site(start_url)