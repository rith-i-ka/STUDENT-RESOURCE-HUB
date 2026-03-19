from scrapers.gitscrap import scrape_github
from scrapers.acadscrap import scrape_academics
from scrapers.internscrap import scrape_internships
from utils.helper import save_to_json, print_data

def main():
    keyword = input("Enter keyword: ")
    print("\nSelect type:")
    print("1. GitHub")
    print("2. Academics")
    print("3. Internships")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        data = scrape_github(keyword)
        save_to_json(data, "github.json")
        print_data("GitHub", data)

    elif choice == "2":
        data = scrape_academics(keyword)
        save_to_json(data, "academics.json")
        print_data("Academics", data)

    elif choice == "3":
        data = scrape_internships(keyword)
        save_to_json(data, "internships.json")
        print_data("Internships", data)

    else:
        print("Invalid choice ❌")

if __name__ == "__main__":
    main()