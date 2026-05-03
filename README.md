# Pre-Call Brief

A web application for Customer Success professionals that pulls real-time company news so you never walk into a customer call unprepared. Built with Python, Flask, and NewsAPI. - part of personal bootcamp projects portfolio.

## Features
- Real-time company news fetched via NewsAPI
- Up to 12 deduplicated, relevancy-sorted articles per search
- Automatic filtering of videos, low-quality domains, and removed articles
- Fallback image for articles with no thumbnail
- Animated spinner on form submit
- Error handling for API failures and timeouts
- Clean card-based design consistent with portfolio design language

## Requirements
- Python 3
- Flask
- python-dotenv
- requests

## Installation
```
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file in the root directory:
```
NEWS_API_KEY=your_newsapi_key_here
DEBUG=1
```
Get a free API key at [newsapi.org](https://newsapi.org)

## How to Run
```
python app.py
```
The app runs at `http://localhost:5000`

## Project Structure
```
pre-call-brief/
├── app.py                  # Flask app, routes, NewsAPI calls
├── .env                    # API key and debug flag (not committed)
├── .gitignore
├── requirements.txt
├── templates/
│   ├── index.html          # Search page
│   └── results.html        # Brief output page
└── static/
    ├── fallback.png        # Fallback image for missing thumbnails
    └── css/
        └── style.css       # Styles
```

## Limitations
- NewsAPI free tier is restricted to localhost — a paid plan or alternative API is required for deployment
- Article quality and relevancy depend entirely on NewsAPI's algorithm
- Only detects news with a public web presence — not internal company data
- Some articles may be truncated mid-description by the source

## Author
Ghaleb Khadra