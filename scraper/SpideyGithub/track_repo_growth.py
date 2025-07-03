import os
import json
from datetime import datetime

def track():
    today = datetime.now().strftime("%Y-%m-%d")
    data_path = f"data/github/{today}/trending.json"
    tracked_dir = "data/github/tracked"
    os.makedirs(tracked_dir, exist_ok=True)

    if not os.path.exists(data_path):
        print("No trending data found for today.")
        return

    with open(data_path, "r") as f:
        repos = json.load(f)

    for repo in repos:
        filename = repo["name"].replace("/", "_") + ".json"
        track_path = os.path.join(tracked_dir, filename)

        entry = {
            "date": today,
            "stars": int(repo["stars"])
        }

        if os.path.exists(track_path):
            with open(track_path, "r") as tf:
                history = json.load(tf)
        else:
            history = []

        # Avoid duplicate date entries
        if not any(e["date"] == today for e in history):
            history.append(entry)

        with open(track_path, "w") as tf:
            json.dump(history, tf, indent=2)

    print(f"Tracked {len(repos)} repos.")

if __name__ == "__main__":
    track()
