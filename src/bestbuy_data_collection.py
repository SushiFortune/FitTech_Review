import requests
from config import api_key

def format_model_name(user_input):
    user_input = user_input.strip().lower()

    if " - " in user_input:
        parts = user_input.split(" - ")
        if len(parts) == 2 and all(parts):
            return user_input
  
    words = user_input.split()
    if len(words) > 1 and "-" not in user_input:
        formatted_model_name = words[0] + " - " + " ".join(words[1:])
        return formatted_model_name
    
    return None


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


def search_model(user_input):
    # Format the user input
    model_name = format_model_name(user_input)
    if not model_name:
        print("Invalid model name format.")
        return None
    
    try:
        data = fetch_product_data(model_name)
        # Filter products to match the exact model name
        products = [product for product in data['products'] if model_name.lower() in product['name'].lower()]
        return products
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

