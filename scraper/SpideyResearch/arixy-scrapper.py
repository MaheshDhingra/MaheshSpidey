import os
import json
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Setup folders
os.makedirs("logs/arxiv_ai", exist_ok=True)
os.makedirs("data/arxiv_ai", exist_ok=True)

# Setup logging
log_path = os.path.join("logs/arxiv_ai", "scraper.log")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MaheshSpidey/1.7; +https://maheshdhingra.xyz)"
}
URL = "https://arxiv.org/list/cs.AI/recent"

def scrape_arxiv_ai():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to fetch arXiv AI papers: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")
    papers = []

    # Each paper is inside a dt/dd pair
    entries = soup.select("dl > dt")
    for dt in entries:
        dd = dt.find_next_sibling("dd")

        id_tag = dt.select_one("a[href^='/abs/']")
        if not id_tag:
            continue
        paper_id = id_tag["href"].split("/")[-1]
        abs_url = f"https://arxiv.org/abs/{paper_id}"
        pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"

        title_tag = dd.find("div", class_="list-title")
        authors_tag = dd.find("div", class_="list-authors")
        abstract_tag = dd.find("p")

        title = title_tag.get_text(strip=True).replace("Title:", "") if title_tag else "No title"
        authors = authors_tag.get_text(strip=True).replace("Authors:", "") if authors_tag else "Unknown"
        abstract = abstract_tag.get_text(strip=True) if abstract_tag else "No abstract"

        papers.append({
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "abs_url": abs_url,
            "pdf_url": pdf_url
        })

    today = datetime.now().strftime("%Y-%m-%d")
    output_file = f"data/arxiv_ai/{today}-papers.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=2, ensure_ascii=False)

    logging.info(f"✅ Scraped {len(papers)} arXiv AI papers to {output_file}")


if __name__ == "__main__":
    scrape_arxiv_ai()
