import os
import json
import subprocess
from datetime import datetime

KAGGLE_USERNAME = "maheshdhingra"
DATASET_SLUG = "github-trending-daily"
DATASET_DIR = "kaggle_dataset"
TITLE = "GitHub Trending Repositories (Daily Scrape)"
DESCRIPTION = "Trending repositories scraped daily from GitHub with metadata."
LICENSES = [{"name": "CC0-1.0"}]

def prepare_dataset_folder():
    """Populate DATASET_DIR with metadata and today's data files."""
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(DATASET_DIR, exist_ok=True)

    # Write dataset-metadata.json
    metadata = {
        "title": TITLE,
        "id": f"{KAGGLE_USERNAME}/{DATASET_SLUG}",
        "licenses": LICENSES,
        "description": DESCRIPTION
    }
    with open(os.path.join(DATASET_DIR, "dataset-metadata.json"), "w") as f:
        json.dump(metadata, f, indent=4)

    # Copy today's files
    today_dir = f"data/{today}"
    for fname in ("trending.json", "top.json"):
        src = os.path.join(today_dir, fname)
        if os.path.exists(src):
            dst = os.path.join(DATASET_DIR, f"{today}_{fname}")
            with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
                fdst.write(fsrc.read())

def kaggle_cmd(action):
    """Run a kaggle CLI command; return subprocess.CompletedProcess."""
    cmd = ["kaggle", "datasets", action, "-p", DATASET_DIR, "-m",
           f"Update on {datetime.now().strftime('%Y-%m-%d')}"]
    if action == "create":
        cmd.insert(3, "-u")
    return subprocess.run(cmd, capture_output=True, text=True)

def upload():
    prepare_dataset_folder()

    # First try versioning
    print("Attempting to create a new dataset version...")
    version = kaggle_cmd("version")
    if version.returncode == 0:
        print("Dataset version updated on Kaggle.")
        return

    print("⚠️ Versioning failed; trying initial dataset creation...")
    create = kaggle_cmd("create")
    if create.returncode == 0:
        print("Dataset created on Kaggle.")
    else:
        print("Kaggle upload failed.")
        print("STDOUT:", create.stdout)
        print("STDERR:", create.stderr)

if __name__ == "__main__":
    upload()
