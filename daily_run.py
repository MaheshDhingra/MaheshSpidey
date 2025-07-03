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

if __name__ == "__main__":
    run_script("scraper/SpideyGithub/github_scraper.py", "GitHub scraper")
    run_script("scraper/SpideyGithub/track_repo_growth.py", "Repo growth tracker")
    run_script("scraper/SpideyYoutube/youtube_scraper.py", "YouTube scraper")
    run_script("scraper/SpideyLandslide/landslide_scrapper.py", "Landslide scraper")
    run_script("scraper/SpideyAmazon/amazon_computer_category_scrapper.py", "Amazon scraper")
