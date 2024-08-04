import requests
from config import api_key

def search_fitbit_sense_2():
    url = "https://api.bestbuy.com/v1/products(search=fitbit sense 2)?format=json"
    params = {
        'apiKey': api_key,
        'show': 'sku,name,salePrice,customerReviewAverage'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['products']
    else:
        return None

products = search_fitbit_sense_2()
if products:
    for product in products:
        print(f"Name: {product['name']}, Rating: {product.get('customerReviewAverage', 'No rating available')}")
else:
    print("No products found.")


    

# sku = '6559662'  
