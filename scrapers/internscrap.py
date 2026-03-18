import requests
from bs4 import BeautifulSoup
from config import INTERNSHIP_URL, HEADERS

def scrape_internships(keyword):
    url = INTERNSHIP_URL + keyword
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    internships = []
    for card in soup.select(".individual_internship")[:5]:
        title = card.select_one(".profile")
        company = card.select_one(".company_name")

        internships.append({
            "role": title.text.strip() if title else "N/A",
            "company": company.text.strip() if company else "N/A"
        })

    return internships