import os
import json
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Setup logging
os.makedirs("logs/landslides", exist_ok=True)
os.makedirs("data/landslides", exist_ok=True)
log_path = os.path.join("logs/landslides", "scraper.log")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MaheshSpidey/1.7; +https://maheshdhingra.xyz)"
}
URL = "https://en.wikipedia.org/wiki/List_of_landslides" 

def scrape_landslides():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to fetch landslide events: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")
    landslides = []

    content = soup.select("h2 ~ ul")
    for section in content:
        for li in section.select("li"):
            text = li.get_text(strip=True)
            links = li.select("a")
            event_link = f"https://en.wikipedia.org{links[0].get('href')}" if links and links[0].get("href", "").startswith("/wiki/") else None
            landslides.append({
                "text": text,
                "link": event_link
            })

    today = datetime.now().strftime("%Y-%m-%d")
    output_file = f"data/landslides/{today}-landslides.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(landslides, f, indent=2, ensure_ascii=False)

    logging.info(f"Scraped {len(landslides)} landslide entries to {output_file}")

if __name__ == "__main__":
    scrape_landslides()