from selenium import webdriver
import time
import os
import requests

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

def search_and_download_first_image(shoe_codes, download_path):
    # Setup the driver
    driver = webdriver.Chrome()  # make sure to set path to chromedriver if not in PATH
    for code in shoe_codes:
        search_url = f'https://www.google.com/search?tbm=isch&q={code}'
        driver.get(search_url)
        time.sleep(3)  # Allow some time for the images to load
        images = driver.find_elements_by_css_selector('img.rg_i.Q4LuWd')  # Update the selector if necessary
        if images:
            image_url = images[0].get_attribute('src')
            filename = os.path.join(download_path, f'{code}.jpg')
            download_image(image_url, filename)
    driver.quit()

# Example list of shoe codes and download directory
shoe_codes = ['12345', '67890', 'ABCDE']
download_path = 'path_to_download_directory'  # Set this to your desired path
search_and_download_first_image(shoe_codes, download_path)
