import requests
import pandas as pd
from bs4 import BeautifulSoup

rokomari_url = 'https://www.rokomari.com/book/category/56/literature'


def rokomari_products(category_url):
    
    response = requests.get(category_url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    
    #products details
    products = []
    product_cards = soup.find_all('div', class_='book-list-wrapper')

    
    for card in product_cards:
        title_tag = card.find('h1', class_='book-title')
        title = title_tag.get_text(strip=True) if title_tag else 'N/A'
        
        rating_tag = card.find('span', class_='book-rating') 
        rating = rating_tag.get_text(strip=True) if rating_tag else 0

      
        price_tag = card.find('p', class_='book-price')
        price = price_tag.get_text(strip=True) if price_tag else 0
        
        
        products.append({
            'Title': title,
            'Rating':rating,
            'Price': price
        })
    
    return products

products = rokomari_products(rokomari_url)


for product in products:
    print(product)
df=pd.DataFrame(products)
df.to_csv('rokomari.csv',index =False)