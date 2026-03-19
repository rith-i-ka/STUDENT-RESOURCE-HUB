import requests
from bs4 import BeautifulSoup

def scrape_internships(keyword):
    url = f"https://internshala.com/internships/{keyword}-internship/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    internships = []

    cards = soup.find_all("div", class_="individual_internship")[:5]

    for card in cards:
        # title
        title_tag = card.find("a", class_="job-title-href")
        title = title_tag.text.strip() if title_tag else "No Title"

        # company (final fix)
        company_tag = card.select_one(".company_name")
        if not company_tag:
            company_tag = card.select_one(".link_display_like_text")
        if not company_tag:
            company_tag = card.find("h4")

        company = company_tag.text.strip() if company_tag else "Unknown Company"

        # link
        link = title_tag["href"] if title_tag else None
        full_link = "https://internshala.com" + link if link else "#"

        internships.append({
            "role": title,
            "company": company,
            "link": full_link
        })

    return internships