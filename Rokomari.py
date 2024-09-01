from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


driver_path = os.path.join(os.getcwd(), 'chromedriver-win64')
exe_path = os.path.join(driver_path, 'chromedriver.exe')

driver = webdriver.Chrome()
driver.maximize_window()


page_url = 'https://www.rokomari.com/book/publisher/586/islamic-foundation'

def fetch_products_from_page(url):
    driver.get(url)
    time.sleep(5)  

    products = driver.find_elements(By.CSS_SELECTOR, 'div.book-text-area')  
 
    product_data = []
    for product in products:
        name_elements = product.find_elements(By.CSS_SELECTOR, 'h4.book-title')  
        author_elements = product.find_elements(By.CSS_SELECTOR, 'p.book-author')  

        name = get_element_text(name_elements[0] if name_elements else None)
        author = get_element_text(author_elements[0] if author_elements else None)

        product_data.append({'Name': name, 'Author Name': author})

    return product_data

def get_next_page_url():
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'body > div.browse-page > div > div > div > section.browse__content > div.pagination > a:nth-child(10)')  # Adjust selector as needed
        return next_button.get_attribute('href')
    except Exception:
        return None

def get_element_text(element, default=''):
    """Helper function to get the text of an element or return a default value."""
    return element.text if element else default



all_products = []


while page_url:
    print(f"Fetching products from: {page_url}")
    products = fetch_products_from_page(page_url)
    all_products.extend(products)
    
    next_page_url = get_next_page_url()
    
    if next_page_url:
        page_url = next_page_url
    else:
        page_url = None
       

df = pd.DataFrame(all_products)
df.to_csv('Rokomari.csv', index=False)
print("Data saved to Rokomari.csv")

driver.quit()