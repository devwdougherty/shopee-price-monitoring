import requests
from bs4 import BeautifulSoup as bs
import time

url = 'https://www.iceloshop.com.br/macbook-pro-m1-pro-14-2-16gb-512ssd'
ret = requests.get(url)
soup = bs(ret.text, 'html.parser')

product_name = soup.find('h1', {'class': 'product-name'}).text

while True:

    product_price = soup.find('h3', {'class': 'mb-0'}).text
    print(f'Seu produto: {product_name} está com o preço {product_price}');
    time.sleep(5)