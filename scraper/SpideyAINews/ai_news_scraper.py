import os
import json
import requests
import logging
from bs4 import BeautifulSoup
from datetime import datetime

# Setup logging
os.makedirs("logs/ainews", exist_ok=True)
log_path = os.path.join("logs", "ainews", "scraper.log")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MaheshSpidey/1.7; +https://maheshdhingra.xyz)"
}
URL = "https://news.google.com/search?q=artificial%20intelligence&hl=en"

def scrape_ai_news():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Request failed: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.select("article"):
        headline_tag = item.select_one("h3")
        if not headline_tag:
            continue

        headline = headline_tag.get_text(strip=True)
        link_tag = headline_tag.find("a")
        link = "https://news.google.com" + link_tag.get("href")[1:] if link_tag else "No link"

        snippet = item.select_one("span")
        summary = snippet.get_text(strip=True) if snippet else "No summary"

        articles.append({
            "headline": headline,
            "summary": summary,
            "link": link
        })

    today = datetime.now().strftime("%Y-%m-%d")
    out_dir = os.path.join("data", "ainews")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{today}-news.json"), "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

    logging.info(f"Scraped {len(articles)} AI news articles to {out_dir}/{today}-news.json")

if __name__ == "__main__":
    scrape_ai_news()
