from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    company = request.form.get("company")

    params = {
        "q": company,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 10,
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    articles = data.get("articles", [])

    return render_template("results.html", company=company, articles=articles)


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG") == "1")