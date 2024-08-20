import requests
from config import api_key


def fetch_product_data(model_name):
    # model_name='garmin-fenix-7s'
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

def filter_data(model_name, data):
    keywords = ["smartwatch", "tracker"]
    filtered_products_v1 = [product for product in data['products'] if model_name.lower() in product['name'].lower()]
    # filtered_products_v2 = [product for product in filtered_products_v1 if any(keyword.lower() in product['name'].lower() for keyword in keywords)]
    return filtered_products_v1

try:
    filtering_model_name='Fitbit - sense 2'
    fetching_model_name = 'fitbit-sense-2'
    data = fetch_product_data(fetching_model_name)
    products=filter_data(filtering_model_name,data)
    print(products)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")





