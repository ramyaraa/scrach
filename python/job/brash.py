import requests
import pandas as pd
import os
import webbrowser
from bs4 import BeautifulSoup
import time

def download_image(url, path, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(path, filename), 'wb') as f:
            f.write(response.content)

def google_search_images(api_key, cse_id, query, download_path):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'cx': cse_id,
        'key': api_key,
        'searchType': 'image',
        'num': 1  # Number of images to fetch
    }
    try:
        response = requests.get(search_url, params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        results = response.json().get('items', [])
        return [item['link'] for item in results]
    except requests.Timeout:
        print("The request timed out. Please try again later.")
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.reason}")
    except requests.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

def search_and_download(api_key, cse_id, code, download_path):
    query = f"shoes_{code}"
    image_links = google_search_images(api_key, cse_id, query, download_path)
    if image_links:
        url = image_links[0]
        filename = f"{code}.jpg"
        download_image(url, download_path, filename)

def open_google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def main():
    api_key = 'AIzaSyBz8QsINjrj6-02_uqbgx8bOkyLmzQd820'
    cse_id = '5750782712c5c49ee'
    df = pd.read_excel('/Users/adam/Desktop/scrach/good.xlsx')  # Path to your Excel file
    shoe_codes = df['Description'].tolist()  # Adjust the column name as needed

    for code in shoe_codes:
        print(f"Searching and downloading for shoe code: {code}")
        search_and_download(api_key, cse_id, code, './downloaded_images')
        time.sleep(2)  # Add a delay to avoid hitting the API rate limit

if __name__ == "__main__":
    main()