import requests
from bs4 import BeautifulSoup

def scrape_internships(keyword):
    url = f"https://www.indeed.com/jobs?q={keyword}+internship"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    internships = []

    for job in soup.select(".job_seen_beacon")[:5]:
        title = job.select_one("h2 a span")
        company = job.select_one(".companyName")
        link = job.select_one("h2 a")

        internships.append({
            "role": title.text.strip() if title else "N/A",
            "company": company.text.strip() if company else "N/A",
            "link": "https://www.indeed.com" + link["href"] if link else "N/A"
        })

    return internships