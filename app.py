from flask import Flask, render_template, request
from dotenv import load_dotenv
from datetime import datetime
import requests
import os

load_dotenv()

app = Flask(__name__)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"

@app.route("/")
def index():
    return render_template("index.html", current_year=datetime.now().year)

@app.route("/results", methods=["POST"])
def results():
    company = request.form.get("company").title()

    params = {
        "q": company,
        "sortBy": "relevancy",
        "language": "en",
        "pageSize": 12,
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    seen = set()
    unique_articles = []
    video_domains = ["yahoo.com", "youtube.com", "youtu.be", "vimeo.com", "dailymotion.com"]
    for article in data.get("articles", []):
        url = article.get("url", "")
        if article.get("title") == ["Removed"]:
            continue
        if article["url"] not in seen and not any(domain in url for domain in video_domains):
            seen.add(article["url"])
            unique_articles.append(article)

    return render_template("results.html", company=company, articles=unique_articles, current_year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG") == "1")