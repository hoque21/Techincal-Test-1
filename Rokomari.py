import requests
from bs4 import BeautifulSoup


rokomari_url = 'https://www.rokomari.com/book/56283/friends-language-grammar-reading-comprehension-writing-composition?ref=jfu_hm' 
def fetch_products(url):
    # Send a request to the website
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Optional: Print the HTML content for debugging
    # print(soup.prettify())  # Uncomment this to see the HTML structure

    # Find all product containers (adjust the selector based on actual HTML structure)
    products = soup.find_all('div', class_='product-item')  # Replace with actual class or tag

    # Check if products were found, print the count for debugging
    if not products:
        print("No products found with the class 'product-item'. Check the HTML structure.")
    
    # Extract product details
    product_list = []
    for product in products:
       
        name_tag = product.find('h2', class_='product-name')  
        price_tag = product.find('span', class_='product-price')  
        
        # Check if the tags are found and extract text
        name = name_tag.text.strip() if name_tag else 'No name found'
        price = price_tag.text.strip() if price_tag else 'No price found'
        
        product_list.append({'name': name, 'price': price})

    return product_list

# URL of the category page (example URL)
 
# Fetch and print products
products = fetch_products(rokomari_url)
if products:
    for product in products:
        print(f"Product Name: {product['name']}, Price: {product['price']}")
else:
    print("No products to display.")
