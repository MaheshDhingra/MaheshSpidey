import os
import json
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Setup
os.makedirs("logs/reddit_ai", exist_ok=True)
os.makedirs("data/reddit_ai", exist_ok=True)

log_path = os.path.join("logs/reddit_ai", "scraper.log")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MaheshSpidey/1.7; +https://maheshdhingra.xyz)"
}

URL = "https://www.reddit.com/r/artificial/top/?t=day"

def scrape_reddit_ai():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to fetch Reddit AI page: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    posts = []

    for post in soup.select("div[data-testid='post-container']"):
        title_tag = post.select_one("h3")
        if not title_tag:
            continue

        title = title_tag.text.strip()
        upvotes = post.select_one("div[data-click-id='score']")
        upvotes = upvotes.text.strip() if upvotes else "0"

        comments_tag = post.select_one("a[data-click-id='comments']")
        comments_text = comments_tag.text.strip() if comments_tag else "0 comments"
        comments = comments_text.split()[0]  # "123 comments" -> "123"

        post_url_tag = post.select_one("a[data-click-id='body']")
        post_url = f"https://www.reddit.com{post_url_tag.get('href')}" if post_url_tag else None

        posts.append({
            "title": title,
            "upvotes": upvotes,
            "comments": comments,
            "url": post_url
        })

    today = datetime.now().strftime("%Y-%m-%d")
    out_path = f"data/reddit_ai/{today}-top.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    logging.info(f"Scraped {len(posts)} Reddit AI posts to {out_path}")


if __name__ == "__main__":
    scrape_reddit_ai()
