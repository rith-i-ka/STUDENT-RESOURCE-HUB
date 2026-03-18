import requests
from bs4 import BeautifulSoup
from config import SCHOLAR_URL, HEADERS

def scrape_academics(keyword):
    url = SCHOLAR_URL + keyword
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    papers = []
    for result in soup.select(".gs_ri")[:5]:
        title = result.select_one(".gs_rt")
        link = title.a["href"] if title and title.a else "N/A"

        papers.append({
            "title": title.text if title else "N/A",
            "link": link
        })

    return papers