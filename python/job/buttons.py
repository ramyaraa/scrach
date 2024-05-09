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
    try:
        print(f"Making a request to URL: {search_url} with parameters: {params}")
        response = requests.get(search_url, params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(f"Response received: {response.status_code}")
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

def main():
    api_key = 'AIzaSyBz8QsINjrj6-02_uqbgx8bOkyLmzQd820'
    cse_id = '5750782712c5c49ee'
    df = pd.read_excel('/Users/adam/Desktop/hi.xlsx')  # Path to your Excel file
    shoe_codes = df['productid'].tolist()  # Adjust the column name as needed

    for code in shoe_codes:
        query = f"shoes_{code}"  # Create a query string for each shoe code
        image_links = google_search_images(api_key, cse_id, query, './downloaded_images')
        download_image(image_links[0], './downloaded_images', f'{code}.jpg')  # Download the first image
    

if __name__ == "__main__":
    main()