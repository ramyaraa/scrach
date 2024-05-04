import webbrowser

def search_shoe_images(shoe_codes):
    base_url = 'https://www.google.com/search?tbm=isch&q='
    for code in shoe_codes:
        search_url = base_url + code
        webbrowser.open_new_tab(search_url)

# Example list of shoe codes
shoe_codes = ['12345', '67890', 'ABCDE']
search_shoe_images(shoe_codes)
