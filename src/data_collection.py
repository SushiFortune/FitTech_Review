import requests
from config import api_key

def search_fitbit_sense_2():
    url = "https://api.bestbuy.com/v1/products(search=fitbit sense 2)?format=json"
    params = {
        'apiKey': api_key,
        'show': 'sku,name,salePrice,customerReviewAverage',
     
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        sense_2_products = [product for product in data['products'] if 'Sense 2' in product['name']]
        return sense_2_products
    else:
        return None


    

# sku = '6559662'  
