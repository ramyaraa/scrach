import requests
import pandas as pd
import os

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
        'num': 10  # Number of images to fetch
    }
    response = requests.get(search_url, params=params)
    results = response.json()
    images = [item['link'] for item in results.get('items', [])]
    for idx, img_url in enumerate(images):
        download_image(img_url, download_path, f"{query}_{idx}.jpg")

def main():
    api_key = 'AIzaSyBz8QsINjrj6-02_uqbgx8bOkyLmzQd820'
    cse_id = '5750782712c5c49ee'
    df = pd.read_excel('/Users/adam/Desktop/hi.xlsx')  # Path to your Excel file
    shoe_codes = df['productid'].tolist()  # Adjust the column name as needed

    for code in shoe_codes:
        google_search_images(api_key, cse_id, code, './downloaded_images')

if __name__ == "__main__":
    main()
