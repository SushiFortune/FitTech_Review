import requests
from config import api_key
from urllib.parse import quote

def fetch_product_data(model_name):
    
    url = f"https://api.bestbuy.com/v1/products(search={model_name})?format=json"
    params = {
        'apiKey': api_key,
        'show': 'sku,name,salePrice,customerReviewAverage',
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def filter_data(data):
   keywords = ["smartwatch", "tracker"]
   filtered_products = [product for product in data['products'] if any(keyword.lower() in product['name'].lower() for keyword in keywords)]
   return filtered_products


try:
   model_name = 'Fitbit - Inspire 3'
   data = fetch_product_data(model_name)
   products=filter_data(data)
   print(products)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
