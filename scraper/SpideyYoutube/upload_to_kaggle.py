import os
import json
import subprocess
from datetime import datetime

KAGGLE_USERNAME = "maheshdhingra"
DATASET_SLUG = "youtube-trending-daily"
DATASET_DIR = "kaggle_dataset/youtube"
TITLE = "YouTube Trending Videos"
DESCRIPTION = "Trending videos scraped daily from YouTube with metadata."
LICENSES = [{"name": "CC0-1.0"}]

def prepare_dataset_folder():
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(DATASET_DIR, exist_ok=True)

    metadata = {
        "title": TITLE,
        "id": f"{KAGGLE_USERNAME}/{DATASET_SLUG}",
        "licenses": LICENSES,
        "description": DESCRIPTION
    }
    with open(os.path.join(DATASET_DIR, "dataset-metadata.json"), "w") as f:
        json.dump(metadata, f, indent=4)

    today_dir = f"data/youtube/{today}"
    for fname in ("trending.json",):
        src = os.path.join(today_dir, fname)
        if os.path.exists(src):
            dst = os.path.join(DATASET_DIR, f"{today}_{fname}")
            with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
                fdst.write(fsrc.read())

def kaggle_cmd(action):
    today_str = datetime.now().strftime('%Y-%m-%d')
    if action == "version":
        return subprocess.run([
            "kaggle", "datasets", "version", "-p", DATASET_DIR, "-m",
            f"Update on {today_str}"
        ], capture_output=True, text=True)
    elif action == "create":
        return subprocess.run([
            "kaggle", "datasets", "create", "-p", DATASET_DIR, "-u", "--public"
        ], capture_output=True, text=True)

def upload():
    prepare_dataset_folder()

    print("Attempting to create a new dataset version...")
    version = kaggle_cmd("version")
    if version.returncode == 0:
        print("YouTube dataset version updated on Kaggle.")
        return

    print("⚠️ Versioning failed; trying initial dataset creation...")
    create = kaggle_cmd("create")
    if create.returncode == 0:
        print("YouTube dataset created on Kaggle.")
    else:
        print("YouTube Kaggle upload failed.")
        print("STDOUT:", create.stdout)
        print("STDERR:", create.stderr)

if __name__ == "__main__":
    upload()