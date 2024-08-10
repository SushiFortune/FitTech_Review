import requests
from config import api_key

def fetch_product_data(model_name):
    # URL encode the model name
    encoded_model_name = requests.utils.quote(model_name.replace(" ", "-"))
    
    url = f"https://api.bestbuy.com/v1/products(search={encoded_model_name})?format=json"
    params = {
        'apiKey': api_key,
        'show': 'sku,name,salePrice,customerReviewAverage',
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Test the function
model_name = "Fitbit - Charge 6 Advanced Fitness & Health Tracker"
try:
    data = fetch_product_data(model_name)
    print("API Response:")
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
