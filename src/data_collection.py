import requests
from config import api_key

def get_review_score(sku):
    url = f"https://api.bestbuy.com/v1/products(sku={sku})"
    params = {
        'apiKey': api_key,
        'format': 'json',
        'show': 'customerReviewAverage'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'products' in data and len(data['products']) > 0:
            return data['products'][0]['customerReviewAverage']
        else:
            return None
    else:
        return None

    

# sku = '6559662'  
