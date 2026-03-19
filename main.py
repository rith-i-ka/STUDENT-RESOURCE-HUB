from flask import Flask, request, jsonify
from scrapers.gitscrap import scrape_github
from scrapers.acadscrap import scrape_academics
from scrapers.internscrap import scrape_internships

app = Flask(__name__)

# Home route (just to check server)
@app.route("/")
def home():
    return "Backend is running 🚀"


# Search route
@app.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("q")
    data_type = request.args.get("type")

    if not keyword or not data_type:
        return jsonify({"error": "Missing keyword or type"}), 400

    if data_type == "github":
        result = scrape_github(keyword)

    elif data_type == "academics":
        result = scrape_academics(keyword)

    elif data_type == "internships":
        result = scrape_internships(keyword)

    else:
        return jsonify({"error": "Invalid type"}), 400

    return jsonify({
        "results": result
    })


if __name__ == "__main__":
    app.run(debug=True)