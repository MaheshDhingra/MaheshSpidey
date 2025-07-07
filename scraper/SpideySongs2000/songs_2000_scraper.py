import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_songs_2000():
    # Billboard Year-End Hot 100 for a year in the 2000s (e.g., 2000)
    # Note: Billboard's site structure can be complex and change frequently.
    # This URL is for 2000, you might need to adjust for other years or a different approach.
    url = "https://www.billboard.com/charts/year-end/2000/hot-100-songs" 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        print(f"Attempting to fetch songs from {url}...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("Songs page fetched successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.text, 'html.parser')

    songs = []
    # Billboard chart items are often within <li> or <div> tags with specific classes.
    # This is a simplified example and might need adjustment based on current site structure.
    for song_tag in soup.find_all('div', class_='o-chart-results-list-row-container'): # Example class
        title_tag = song_tag.find('h3', id='title-of-a-story') # Example ID
        artist_tag = song_tag.find('span', class_='c-label') # Example class for artist
        
        title = title_tag.text.strip() if title_tag else "No Title"
        artist = artist_tag.text.strip() if artist_tag else "No Artist"
        
        songs.append({"Title": title, "Artist": artist})

    df = pd.DataFrame(songs)
    return df

def run_script(output_dir="data/songs_2000"):
    print("Running Songs 2000 scraper...")
    df = scrape_songs_2000()
    
    if not df.empty:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "songs_2000_data.csv")
        df.to_csv(output_path, index=False)
        print(f"Songs 2000 data saved to {output_path}")
    else:
        print("No songs 2000 data scraped.")

if __name__ == "__main__":
    run_script()
