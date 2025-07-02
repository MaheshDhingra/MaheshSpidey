# GitHub Trending Scraper

A Python web scraper that fetches GitHub's trending repositories daily, respects `robots.txt`, and saves the data in a structured directory for analysis or public use.

---

## Objective

Track trending repositories on GitHub daily and store them in structured JSON files for further analysis or open data sharing.

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

## Usage

### Run scraper once:

```bash
python scraper/github_scraper.py --today-only
```

### Print today's top trending repo:

```bash
python scraper/github_scraper.py --top
```

### Run scraper with daily scheduling (runs scraping at 10:00 AM daily):

```bash
python scraper/github_scraper.py
```

> *Note:* The scheduled run will keep the process running and scrape daily at 10:00 AM.

---

## Directory Structure

```plaintext
github-trending-scraper/
├── data/
│   ├── 2025-07-02/
│   │   ├── trending.json     # Full list of trending repos for the day
│   │   └── top.json          # Top starred repo for the day
│   ├── 2025-07-03/
│   │   ├── trending.json
│   │   └── top.json
│   └── tracked/              # Historical growth tracking per repo
│       ├── microsoft_generative-ai-for-beginners.json
│       └── ...
├── logs/
│   └── scraper.log           # Log file for errors and events
├── scraper/
│   └── github_scraper.py     # Main scraper script with CLI & scheduling support
├── track_repo_growth.py      # Script to track repo star growth over time
├── upload_to_kaggle.py       # Script to upload datasets to Kaggle
├── daily_run.py              # Script to run scraper, tracker, and uploader sequentially
├── requirements.txt          # Python dependencies
└── README.md                 # This documentation
```

---

## Ethical Considerations

* Respects `robots.txt` before crawling
* Uses a custom, identifiable User-Agent header
* Handles errors and logs events for transparency

---

## Additional Tools

* **`track_repo_growth.py`** — Tracks star growth for each repo over time
* **`upload_to_kaggle.py`** — Automates uploading daily datasets to Kaggle
* **`daily_run.py`** — Runs the scraper, tracker, and Kaggle uploader in sequence

---

## Future Improvements

* Add notifications for trending repo changes
* Support scraping multiple GitHub trending languages or timeframes
* Integrate with dashboards or visualization tools

---

Feel free to contribute or open issues for bugs and feature requests!
Happy scraping!
