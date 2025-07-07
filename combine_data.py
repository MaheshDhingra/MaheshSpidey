import json
import csv
import os
from datetime import datetime

def combine_data_to_csv():
    all_data = []
    today = datetime.now().strftime("%Y-%m-%d")

    # Arxiv AI data
    arxiv_path = f"data/arxiv_ai/{today}-papers.json"
    if os.path.exists(arxiv_path):
        with open(arxiv_path, 'r') as f:
            arxiv_data = json.load(f)
            for item in arxiv_data:
                all_data.append({
                    "source": "arxiv_ai",
                    "title": item.get("title"),
                    "description": item.get("abstract"),
                    "authors": item.get("authors"),
                    "url": item.get("abs_url"),
                    "stars": None,
                    "date": today
                })

    # Github trending data
    github_trending_path = f"data/github/{today}/trending.json"
    if os.path.exists(github_trending_path):
        with open(github_trending_path, 'r') as f:
            github_data = json.load(f)
            for item in github_data:
                all_data.append({
                    "source": "github",
                    "title": item.get("name"),
                    "description": item.get("description"),
                    "authors": None,
                    "url": f"https://github.com/{item.get('name')}",
                    "stars": item.get("stars"),
                    "date": today
                })

    # Define CSV file path
    output_csv_path = "kaggle_data.csv"

    # Write to CSV
    if all_data:
        keys = all_data[0].keys()
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(all_data)
        print(f"Successfully combined data into {output_csv_path}")
    else:
        print("No data found to combine.")

if __name__ == "__main__":
    combine_data_to_csv()
