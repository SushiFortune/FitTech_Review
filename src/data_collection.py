import requests
from config import api_key

def format_model_name(user_input):
    # Validate user input
    if " - " in user_input:
        return user_input
    words = user_input.split()
    if len(words) > 1:
        formatted_model_name = words[0] + " - " + " ".join(words[1:])
    else:
        return None
    return formatted_model_name

def search_model(user_input):
    # Format the model name
    model_name = format_model_name(user_input)
    url = f"https://api.bestbuy.com/v1/products(search={model_name})?format=json"
    params = {
        'apiKey': api_key,
        'show': 'sku,name,salePrice,customerReviewAverage',
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data) 
        # Filter products to match the exact model name
        products = [product for product in data['products'] if model_name.lower() in product['name'].lower()]
        return products
    else:
        return None

