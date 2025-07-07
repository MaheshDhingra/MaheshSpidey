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

    # AI News data
    ainews_path = f"data/ainews/{today}-news.json"
    if os.path.exists(ainews_path):
        with open(ainews_path, 'r') as f:
            ainews_data = json.load(f)
            for item in ainews_data:
                all_data.append({
                    "source": "ainews",
                    "title": item.get("headline"),
                    "description": item.get("summary"),
                    "authors": None,
                    "url": item.get("link"),
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

    # Landslides data
    landslides_path = f"data/landslides/{today}-landslides.json"
    if os.path.exists(landslides_path):
        with open(landslides_path, 'r') as f:
            landslides_data = json.load(f)
            for item in landslides_data:
                all_data.append({
                    "source": "landslides",
                    "title": None, # No specific title, description is the main text
                    "description": item.get("text"),
                    "authors": None,
                    "url": item.get("link"),
                    "stars": None,
                    "date": today
                })

    # Reddit AI data
    reddit_ai_path = f"data/reddit_ai/{today}-top.json"
    if os.path.exists(reddit_ai_path):
        with open(reddit_ai_path, 'r') as f:
            reddit_ai_data = json.load(f)
            for item in reddit_ai_data:
                all_data.append({
                    "source": "reddit_ai",
                    "title": item.get("title"),
                    "description": f"Upvotes: {item.get('upvotes')}, Comments: {item.get('comments')}",
                    "authors": None,
                    "url": item.get("url"),
                    "stars": item.get("upvotes"), # Using upvotes as stars
                    "date": today
                })

    # Youtube trending data
    youtube_trending_path = f"data/youtube/{today}/trending.json"
    if os.path.exists(youtube_trending_path):
        with open(youtube_trending_path, 'r') as f:
            youtube_data = json.load(f)
            for item in youtube_data:
                all_data.append({
                    "source": "youtube",
                    "title": item.get("title"),
                    "description": f"Channel: {item.get('channel')}, Views: {item.get('views')}, Duration: {item.get('duration')}",
                    "authors": item.get("channel"),
                    "url": None, # YouTube scraper doesn't provide direct video URL
                    "stars": None, # No direct star equivalent
                    "date": today
                })

    # Amazon products data (from CSV)
    amazon_products_path = "data/products.csv"
    if os.path.exists(amazon_products_path):
        with open(amazon_products_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for item in reader:
                # Extract the dynamic price header
                price_key = next((key for key in item.keys() if "Price" in key), None)
                
                all_data.append({
                    "source": "amazon",
                    "title": item.get("Name"),
                    "description": f"Price: {item.get(price_key, 'N/A')}, Reviews: {item.get('Number of Reviews', 'N/A')}",
                    "authors": None,
                    "url": f"https://www.amazon.com/dp/{item.get('Asin')}" if item.get('Asin') else None,
                    "stars": None, # No direct star equivalent
                    "date": today
                })

    # Company Fraud data
    company_fraud_path = f"data/companyfraud/{today}-data.json"
    if os.path.exists(company_fraud_path):
        with open(company_fraud_path, 'r') as f:
            company_fraud_data = json.load(f)
            for item in company_fraud_data:
                all_data.append({
                    "source": "company_fraud",
                    "title": item.get("title"),
                    "description": item.get("summary"),
                    "authors": None,
                    "url": item.get("link"),
                    "stars": None,
                    "date": today
                })

    # Government Fights data
    government_fights_path = f"data/governmentfights/{today}-data.json"
    if os.path.exists(government_fights_path):
        with open(government_fights_path, 'r') as f:
            government_fights_data = json.load(f)
            for item in government_fights_data:
                all_data.append({
                    "source": "government_fights",
                    "title": item.get("title"),
                    "description": item.get("summary"),
                    "authors": None,
                    "url": item.get("link"),
                    "stars": None,
                    "date": today
                })

    # Movies 1990 data
    movies_1990_path = f"data/movies1990/{today}-data.json"
    if os.path.exists(movies_1990_path):
        with open(movies_1990_path, 'r') as f:
            movies_1990_data = json.load(f)
            for item in movies_1990_data:
                all_data.append({
                    "source": "movies_1990",
                    "title": item.get("title"),
                    "description": item.get("summary"),
                    "authors": None,
                    "url": item.get("link"),
                    "stars": None,
                    "date": today
                })

    # Songs 2000 data
    songs_2000_path = f"data/songs2000/{today}-data.json"
    if os.path.exists(songs_2000_path):
        with open(songs_2000_path, 'r') as f:
            songs_2000_data = json.load(f)
            for item in songs_2000_data:
                all_data.append({
                    "source": "songs_2000",
                    "title": item.get("title"),
                    "description": item.get("summary"),
                    "authors": None,
                    "url": item.get("link"),
                    "stars": None,
                    "date": today
                })

    # Tech Market data
    tech_market_path = f"data/techmarket/{today}-data.json"
    if os.path.exists(tech_market_path):
        with open(tech_market_path, 'r') as f:
            tech_market_data = json.load(f)
            for item in tech_market_data:
                all_data.append({
                    "source": "tech_market",
                    "title": item.get("title"),
                    "description": item.get("summary"),
                    "authors": None,
                    "url": item.get("link"),
                    "stars": None,
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
