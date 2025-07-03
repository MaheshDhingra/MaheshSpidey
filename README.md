# MaheshSpidey 1.4.3

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
MaheshSpidey/
├── data/
│   ├── github/
│   │   ├── 2025-07-03/
│   │   │   ├── trending.json
│   │   │   └── top.json
│   │   └── tracked/             
│   ├── youtube/
│   │   └── 2025-07-03/
│   │       └── trending.json   
├── logs/
│   ├── github/
│   │   └── scraper.log
│   └── youtube/
│       └── scraper.log
├── scraper/
│   ├── SpideyGithub/
│   │   ├── github_scraper.py
│   │   └── track_repo_growth.py
│   ├── SpideyAmazon/
│   │   └── amazon_computer_category_scrapper.py.py 
│   ├── SpideyLandslide/
│   │   └── landslide_scrapper.py 
│   └── SpideyYoutube/
│       └── youtube_scraper.py
├── daily_run.py
├── requirements.txt
└── README.md
```

---
