import requests_html
from requests_html import HTMLSession, AsyncHTMLSession
from bs4 import BeautifulSoup
from time import sleep
from random import uniform
import pandas as pd


session = HTMLSession()

def parse_data(url):
    name = []
    types = []
    prices = []
    ratings = []
    reviews = []
    image_link = []
    
    resp = session.get(url)
    resp_html = resp.html.render(sleep = 1, keep_page = True, scrolldown = 5)
    resp_html = resp.html.html
    soup = BeautifulSoup(resp_html, 'lxml')
    product_body = soup.find_all('div', class_ = 'product-contents')
    for product in product_body:
        title = product.find('a', class_ = 'product-title').get_text().strip()
        prod_type = product.find('div', class_  = 'product-type').get_text().strip()
        price = product.find('div', class_ = 'product-price').get_text().strip()
        rating = product.find('span', class_ = 'sr-only').get_text().strip()
        review = product.find('a', class_ = 'text-m').get_text().strip()

        name.append(title)
        types.append(prod_type)
        prices.append(price)
        ratings.append(rating)
        reviews.append(review)


    df = pd.DataFrame({'Product Name':name, 'Product Type':prod_type,
                       'Price':prices, 'Rating':ratings,
                       'Reviews':reviews})
    df.to_csv('Kylie lips.csv', index = False)
    print(df.head(5))

parse_data('https://www.kyliecosmetics.com/collections/lips')   #you can change the link  
