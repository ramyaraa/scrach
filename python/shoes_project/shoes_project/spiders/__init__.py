import scrapy
from scrapy.http import Request
import pandas as pd
import os

class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    
    def start_requests(self):
        # Assuming the Excel file is in the same directory as your scrapy project root
        df = pd.read_excel('../../shoe_codes.xlsx')  # Update the file path as needed
        shoe_codes = df['shoe_code_column'].tolist()  # Update the column name
        for code in shoe_codes:
            url = f'https://www.google.com/search?q={code}&tbm=isch'
            yield Request(url, self.parse, meta={'shoe_code': code})

    def parse(self, response):
        images = response.css('img::attr(src)').getall()
        for img_url in images:
            file_name = f"{response.meta['shoe_code']}_{images.index(img_url)}.jpg"
            file_path = os.path.join('../../images', file_name)  # Save images in an 'images' folder at project root
            yield Request(img_url, self.save_image, meta={'file_path': file_path})

    def save_image(self, response):
        with open(response.meta['file_path'], 'wb') as f:
            f.write(response.content)
