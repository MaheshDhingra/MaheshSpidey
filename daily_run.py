import subprocess
import sys

def run_scraper():
    print("🕸️ Running GitHub scraper...")
    result = subprocess.run([sys.executable, "scraper/github_scraper.py", "--today-only"])
    if result.returncode != 0:
        print("❌ Scraper failed")
        return False
    return True

def run_tracker():
    print("📈 Tracking repo growth...")
    result = subprocess.run([sys.executable, "scraper/track_repo_growth.py"])
    if result.returncode != 0:
        print("❌ Tracker failed")
        return False
    return True

def run_kaggle_upload():
    print("📤 Uploading dataset to Kaggle...")
    result = subprocess.run([sys.executable, "scraper/upload_to_kaggle.py"])
    if result.returncode != 0:
        print("❌ Kaggle upload failed")
        return False
    return True

def main():
    if run_scraper():
        if run_tracker():
            run_kaggle_upload()

if __name__ == "__main__":
    main()
