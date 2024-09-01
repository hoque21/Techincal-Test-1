import requests
from bs4 import BeautifulSoup


def scrape_rokomari(url):
    
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the product names and prices (this can change depending on the site structure)
        products = soup.find_all('div', class_='product-item')
        
        if products:
            for product in products:
                # Example of extracting title and price (selectors may vary)
                title = product.find('h1', class_='book-title').text.strip()
               
                print(f"Product: {title}")
        else:
            # Handle if no products are found
            print("No products found on the page.")
    else:
        print("Failed to retrieve the webpage")

# Example usage
url = 'https://www.rokomari.com/book/56283/friends-language-grammar-reading-comprehension-writing-composition'

scrape_rokomari(url)
