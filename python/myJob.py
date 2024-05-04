import pandas as pd
from selenium import webdriver
import time
import os
import requests
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

def search_and_download_first_image(shoe_codes, download_path):
    driver = webdriver.Chrome()  # make sure to set path to chromedriver if not in PATH
    images_paths = []
    for code in shoe_codes:
        search_url = f'https://www.google.com/search?tbm=isch&q={code}'
        driver.get(search_url)
        time.sleep(3)  # Allow some time for the images to load
        images = driver.find_elements_by_css_selector('img.rg_i.Q4LuWd')  # Update the selector if necessary
        if images:
            image_url = images[0].get_attribute('src')
            filename = os.path.join(download_path, f'{code}.jpg')
            download_image(image_url, filename)
            images_paths.append(filename)
        else:
            images_paths.append('')
    driver.quit()
    return images_paths

def embed_images_in_excel(file_path, images_paths):
    wb = load_workbook(file_path)
    ws = wb.active  # Assumes you're working with the first sheet
    img_column = 'C'  # Specify the column to insert images
    for index, img_path in enumerate(images_paths, start=2):  # Adjust start based on your Excel row start
        if os.path.exists(img_path):
            img = Image(img_path)
            img.anchor = f'{img_column}{index}'  # Sets the position of the image
            ws.add_image(img)
    wb.save(file_path)

# Example usage
excel_path = 'path_to_your_excel_file.xlsx'
shoe_codes = read_shoe_codes_from_excel(excel_path)
download_path = 'path_to_download_directory'
images_paths = search_and_download_first_image(shoe_codes, download_path)
embed_images_in_excel(excel_path, images_paths)
