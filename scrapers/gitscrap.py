import requests
from config import GITHUB_URL, HEADERS

def scrape_github(keyword):
    url = GITHUB_URL + keyword
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    repos = []
    for item in data.get("items", [])[:10]:
        repos.append({
            "name": item["name"],
            "url": item["html_url"],
            "stars": item["stargazers_count"]
        })

    return repos