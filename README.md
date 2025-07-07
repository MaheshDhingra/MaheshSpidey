<p align="center">
  <img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/359224e618d7650914d1c5e43f09c26dce6e74b3_index_-_mahesh__1_.png" alt="MaheshSpidey Banner" width="100%">
</p>

# MaheshSpidey 1.8.4

A Python web scraper that fetches data from various sources including GitHub, YouTube, LinkedIn, Arxiv, and movie/song databases. It stores the data in structured directories, respects `robots.txt`, and uploads the datasets to Kaggle.

Scraped data:
https://www.kaggle.com/datasets/maheshdhingra/youtube-trending
https://www.kaggle.com/datasets/maheshdhingra/research-papers
https://www.kaggle.com/datasets/maheshdhingra/movies-year
https://www.kaggle.com/datasets/maheshdhingra/song-year
https://www.kaggle.com/datasets/maheshdhingra/github-top
https://www.kaggle.com/datasets/maheshdhingra/github-trending
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
│   ├── arxiv_ai/
│   │   └── 2025-07-08-papers.json
│   ├── github/
│   │   ├── 2025-07-08/
│   │   │   ├── top.json
│   │   │   └── trending.json
│   │   └── tracked/
│   │       ├── anthropics_prompt-eng-interactive-tutorial.json
│   │       ├── CodeWithHarry_Sigma-Web-Dev-Course.json
│   │       ├── commaai_openpilot.json
│   │       ├── dockur_macos.json
│   │       ├── ed-donner_llm_engineering.json
│   │       ├── humanlayer_12-factor-agents.json
│   │       ├── pocketbase_pocketbase.json
│   │       ├── rustfs_rustfs.json
│   │       ├── smallcloudai_refact.json
│   │       └── th-ch_youtube-music.json
│   ├── movies/
│   │   ├── movies_0.csv
│   │   ├── movies_1998.csv
│   │   ├── movies_2017.csv
│   │   └── movies_2018.csv
│   └── songs_2000/
│       └── songs_2000_data.csv
├── logs/
│   └── youtube/
│       └── scraper.log
├── scraper/
│   ├── SpideyGithub/
│   │   ├── github_scraper.py
│   │   └── track_repo_growth.py
│   ├── SpideyLinked/
│   │   └── linked_tech_jobs.py
│   ├── SpideyMovie/
│   │   └── movie_scrapper.py
│   ├── SpideyResearch/
│   │   └── arixy-scrapper.py
│   ├── SpideySongs2000/
│   │   └── songs_2000_scraper.py
│   └── SpideyYoutube/
│       └── youtube_scraper.py
├── requirements.txt
└── README.md
