import requests
from config import api_key
from urllib.parse import quote

def fetch_product_data(model_name):
    # URL encode the model name
    
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


def filter_results(results, keywords):
    filtered_results = []
    for result in results:
        for keyword in keywords:
            if keyword.lower() in result.lower():
                filtered_results.append(result)
                break

model_name = 'Fitbit - Versa 4 Fitness Smartwatch'

try:
    results = fetch_product_data(model_name)
    keywords = ["smartwatch", "tracker"]
    filtered_results=filter_results(results,keywords)

    print("API Response:")
    for result in filtered_results:
        print(result)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
