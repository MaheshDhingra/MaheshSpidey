import os
import json
import requests
import logging
import argparse
import schedule
import time
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.robotparser import RobotFileParser

# Setup logging
log_path = os.path.join("logs", "scraper.log")
os.makedirs("logs/github/", exist_ok=True)
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MaheshSpidey/1.7; +https://maheshdhingra.xyz)"
}
URL = "https://github.com/trending"


def allowed_by_robots(url):
    rp = RobotFileParser()
    rp.set_url("https://github.com/robots.txt")
    rp.read()
    return rp.can_fetch(HEADERS["User-Agent"], url)


def scrape_github_trending():
    if not allowed_by_robots(URL):
        logging.warning("Access to trending page disallowed by robots.txt.")
        return [], None

    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to fetch GitHub Trending: {e}")
        return [], None

    soup = BeautifulSoup(response.text, "lxml")
    repos = []

    for repo in soup.select("article.Box-row"):
        repo_link = repo.select_one("h2 a")
        if not repo_link:
            continue

        title = repo_link.get("href").strip("/")
        description = repo.p.get_text(strip=True) if repo.p else "No description"
        stars_tag = repo.select_one("a[href$='/stargazers']")
        stars = stars_tag.get_text(strip=True).replace(",", "") if stars_tag else "0"

        repos.append({
            "name": title,
            "description": description,
            "stars": stars
        })

    # Save all repos
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(f"data/github/{today}", exist_ok=True)
    with open(f"data/github/{today}/trending.json", "w") as f:
        json.dump(repos, f, indent=2)

    # Save top repo
    top_repo = None
    if repos:
        top_repo = max(repos, key=lambda r: int(r["stars"]))
        with open(f"data/github/{today}/top.json", "w") as f:
            json.dump(top_repo, f, indent=2)
        logging.info(f"Top repo: {top_repo['name']} with {top_repo['stars']} stars")

    logging.info(f"Scraped {len(repos)} repositories to data/github/{today}/trending.json")
    return repos, top_repo


def run_daily():
    logging.info("📅 Running scheduled scrape task.")
    scrape_github_trending()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", action="store_true", help="Print the top trending repo for today")
    parser.add_argument("--today-only", action="store_true", help="Only scrape today's trending list once")
    args = parser.parse_args()

    if args.today_only or args.top:
        repos, top_repo = scrape_github_trending()

        if args.top and top_repo:
            print("\n Top Trending Repo Today")
            print(json.dumps(top_repo, indent=2))
    else:
        scrape_github_trending()
