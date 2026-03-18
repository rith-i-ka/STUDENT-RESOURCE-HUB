from scrapers.gitscrap import scrape_github
from scrapers.acadscrap import scrape_academics
from scrapers.internscrap import scrape_internships
from utils.helper import save_to_json, print_data

def main():
    keyword = input("Enter keyword: ")

    github_data = scrape_github(keyword)
    acad_data = scrape_academics(keyword)
    intern_data = scrape_internships(keyword)

    save_to_json(github_data, "github.json")
    save_to_json(acad_data, "academics.json")
    save_to_json(intern_data, "internships.json")

    print_data("GitHub", github_data)
    print_data("Academics", acad_data)
    print_data("Internships", intern_data)

if __name__ == "__main__":
    main()