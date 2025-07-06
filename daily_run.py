import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def run_script(path, label):
    logging.info(f"Running {label}...")
    result = subprocess.run(["python", path])
    if result.returncode == 0:
        logging.info(f"{label} finished successfully")
    else:
        logging.error(f"{label} failed")

def run_all():
    run_script("scraper/SpideyGithub/github_scraper.py", "GitHub scraper")
    run_script("scraper/SpideyGithub/track_repo_growth.py", "GitHub growth tracker")
    run_script("scraper/SpideyYoutube/youtube_scraper.py", "YouTube scraper")
    run_script("scraper/SpideyGithub/upload_to_kaggle.py", "GitHub Kaggle uploader")
    run_script("scraper/SpideyYoutube/upload_to_kaggle.py", "YouTube Kaggle uploader")
    run_script("scraper/SpideyLandslides/landslide_scraper.py", "Landslide scraper")
    run_script("scraper/SpideyAINews/ai_news_scraper.py", "AI News scraper")
    run_script("scraper/SpideyTechMarket/tech_market_scraper.py", "Tech Market scraper")
    run_script("scraper/SpideyCompanyFraud/company_fraud_scraper.py", "Company Fraud scraper")
    run_script("scraper/SpideyGovernmentFights/government_fights_scraper.py", "Government Fights scraper")
    run_script("scraper/SpideyMovies1990/movies_1990_scraper.py", "Movies 1990 scraper")
    run_script("scraper/SpideySongs2000/songs_2000_scraper.py", "Songs 2000 scraper")
if __name__ == "__main__":
    run_all()
