import os
import json
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.robotparser import RobotFileParser

# Logging setup
os.makedirs("logs/youtube", exist_ok=True)
log_path = os.path.join("logs", "youtube", "scraper.log")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MaheshSpidey/1.5; +https://maheshdhingra.xyz)"
}
URL = "https://www.youtube.com/feed/trending"

def allowed_by_robots(url):
    rp = RobotFileParser()
    rp.set_url("https://www.youtube.com/robots.txt")
    rp.read()
    return rp.can_fetch(HEADERS["User-Agent"], url)

def scrape_youtube_trending():
    if not allowed_by_robots(URL):
        logging.warning("Disallowed by robots.txt")
        return

    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Request failed: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    scripts = soup.find_all("script")
    initial_data_script = next(
        (s for s in scripts if "var ytInitialData" in s.text), None)

    if not initial_data_script:
        logging.error("ytInitialData not found")
        return

    try:
        raw_json = initial_data_script.string
        json_str = raw_json.split("var ytInitialData = ")[1].split(";</script>")[0]
        data = json.loads(json_str)
    except Exception as e:
        logging.error(f"Failed to parse ytInitialData: {e}")
        return

    videos = []
    try:
        contents = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]\
            ["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]\
            ["itemSectionRenderer"]["contents"][0]["shelfRenderer"]["content"]\
            ["expandedShelfContentsRenderer"]["items"]

        for video in contents[:15]:
            renderer = video.get("videoRenderer", {})
            title = renderer.get("title", {}).get("runs", [{}])[0].get("text", "No title")
            channel = renderer.get("ownerText", {}).get("runs", [{}])[0].get("text", "Unknown channel")
            views = renderer.get("viewCountText", {}).get("simpleText", "No views")
            length = renderer.get("lengthText", {}).get("simpleText", "Unknown duration")

            videos.append({
                "title": title,
                "channel": channel,
                "views": views,
                "duration": length
            })

    except Exception as e:
        logging.error(f"Error parsing video list: {e}")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    out_dir = os.path.join("data", "youtube", today)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "trending.json"), "w", encoding="utf-8") as f:
        json.dump(videos, f, indent=2, ensure_ascii=False)

    logging.info(f"Scraped {len(videos)} trending videos to {out_dir}/trending.json")

if __name__ == "__main__":
    scrape_youtube_trending()
