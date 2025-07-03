# 🕸️ GitHub + YouTube Trending Scraper

A Python web scraper that fetches trending repositories from GitHub and trending videos from YouTube daily. It stores the data in structured directories, respects `robots.txt`, and uploads the datasets to Kaggle.

---

## Objective

Track trending GitHub repositories and YouTube videos daily for open analysis, historical growth tracking, and data sharing.

---

## Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/github-trending-scraper.git
cd github-trending-scraper

# Install dependencies
pip install -r requirements.txt
```

---

## Project Structure

```bash
github-trending-scraper/
├── data/
│   ├── github/
│   │   ├── 2025-07-03/
│   │   │   ├── trending.json     # GitHub trending repos
│   │   │   └── top.json          # Top GitHub repo
│   │   └── tracked/              # Historical growth tracker
│   ├── youtube/
│   │   └── 2025-07-03/
│   │       └── trending.json     # YouTube trending videos
├── kaggle_dataset/
│   └── github/
│       └── dataset-metadata.json
│   └── youtube/
│       └── dataset-metadata.json
├── logs/
│   ├── github/
│   │   └── scraper.log
│   └── youtube/
│       └── scraper.log
├── scraper/
│   ├── SpideyGithub/
│   │   ├── github_scraper.py
│   │   ├── track_repo_growth.py
│   │   └── upload_to_kaggle.py
│   └── SpideyYoutube/
│       ├── youtube_scraper.py
│       └── upload_to_kaggle.py
├── daily_run.py
├── requirements.txt
└── README.md
```

---
