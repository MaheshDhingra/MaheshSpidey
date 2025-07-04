<p align="center">
  <img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/359224e618d7650914d1c5e43f09c26dce6e74b3_index_-_mahesh__1_.png" alt="MaheshSpidey Banner" width="100%">
</p>

# MaheshSpidey 1.7.3

A Python web scraper that fetches trending repositories from GitHub and trending videos from YouTube daily. It stores the data in structured directories, respects `robots.txt`, and uploads the datasets to Kaggle.

---

## Objective

Track trending GitHub repositories and YouTube videos daily for open analysis, historical growth tracking, and data sharing.

---

## Setup

```bash
# Clone the repo
git clone https://github.com/MaheshDhingra/MaheshSpidey.git
cd MaheshSpidey

# Install dependencies
pip install -r requirements.txt
```

---

## Project Structure

```bash
MaheshSpidey/
├── data/
│   ├── github/
│   │   ├── 2025-07-03-trending.json
│   │   ├── 2025-07-03-top.json
│   │   └── tracked/
│   ├── youtube/
│   │   └── 2025-07-03-trending.json
│   ├── landslides/
│   │   └── 2025-07-03-landslides.json
│   ├── ainews/
│   │   └── 2025-07-03-news.json
│   └── amazon/
│       └── 2025-07-03-computers.json
├── kaggle_dataset/
│   └── github/
│       └── dataset-metadata.json
│   └── youtube/
│       └── dataset-metadata.json
├── logs/
│   ├── github/
│   │   └── scraper.log
│   ├── youtube/
│   │   └── scraper.log
│   ├── landslides/
│   │   └── scraper.log
│   └── ainews/
│       └── scraper.log
├── scraper/
│   ├── SpideyGithub/
│   │   ├── github_scraper.py
│   │   ├── track_repo_growth.py
│   │   └── upload_to_kaggle.py
│   ├── SpideyYoutube/
│   │   ├── youtube_scraper.py
│   │   └── upload_to_kaggle.py
│   ├── SpideyLandslide/
│   │   └── landslide_scrapper.py
│   ├── SpideyAINews/
│   │   └── ai_news_scraper.py
│   └── SpideyAmazon/
│       └── amazon_computer_category_scrapper.py
├── daily_run.py
├── requirements.txt
└── README.md
```

---
