import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import base64
import os
import requests
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def download_image(url, filename):
    if url.startswith('http'):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
            else:
                print(f"Failed to download: {url} (Status code: {response.status_code})")
        except requests.RequestException as e:
            print(f"Request failed: {e}, URL: {url}")
    elif url.startswith('data:image'):
        header, encoded = url.split(',', 1)
        data = base64.b64decode(encoded)
        with open(filename, 'wb') as f:
            f.write(data)
    else:
        print("URL is not valid or supported for downloading:", url)

def search_and_download_first_image(shoe_codes, download_path):
    driver = webdriver.Chrome()  # Make sure the path is correct or it's in your PATH
    images_paths = []
    for code in shoe_codes:
        search_url = f'https://www.google.com/search?tbm=isch&q={code}'
        driver.get(search_url)
        time.sleep(4)  # Increase sleep time to ensure images load
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)  # Additional wait after scrolling
        images = driver.find_elements(By.CSS_SELECTOR, 'img.Q4LuWd')
        if images:
            image_url = images[0].get_attribute('src')
            print("Found image URL:")
            filename = os.path.join(download_path, f'{code}.jpg')
            download_image(image_url, filename)
            images_paths.append(filename)
        else:
            images_paths.append('')
            print("No image found for code:", code)
    driver.quit()
    return images_paths

def embed_images_in_excel(file_path, images_paths):
    wb = load_workbook(file_path)
    ws = wb.active  # Assumes you're working with the first sheet
    img_column = 'A'  # Specify the column to insert images
    for index, img_path in enumerate(images_paths, start=2):  # Start from row 2
        if os.path.exists(img_path):
            img = Image(img_path)
            img.anchor = f'{img_column}{index}'  # Sets the position of the image
            ws.add_image(img)
        else:
            print("Image file not found:", img_path)
    wb.save(file_path)

def read_shoe_codes_from_excel(file_path):
    df = pd.read_excel(file_path)
    column_name = 'Material'  # Change to your column name
    if column_name in df.columns:
        return df[column_name].tolist()
    else:
        raise ValueError(f"Column {column_name} not found in Excel file.")


# Example usage
excel_path = '/Users/adam/Desktop/test.xlsx'
shoe_codes = read_shoe_codes_from_excel(excel_path)
download_path = '/Users/adam/Desktop'
images_paths = search_and_download_first_image(shoe_codes, download_path)
embed_images_in_excel(excel_path, images_paths)
