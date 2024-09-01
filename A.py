import requests
from bs4 import BeautifulSoup

# Function to scrape data from a given URL
def scrape_rokomari(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the product names and prices (this can change depending on the site structure)
        products = soup.find_all('div', class_='product-item')
        
        for product in products:
            # Example of extracting title and price (selectors may vary)
            title = product.find('h4', class_='book-title').text.strip()
            price = product.find('p', class_='book-price').text.strip()
            
            print(f"Product: {title}, Price: {price}")
    else:
        print("Failed to retrieve the webpage")

# Example usage
scrape_rokomari('https://www.rokomari.com/book/56283/friends-language-grammar-reading-comprehension-writing-composition?ref=jfu_hm')
