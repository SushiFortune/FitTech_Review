import requests

def get_review_score(api_key, sku):
    url = f"https://api.bestbuy.com/v1/products(sku={sku})"
    params = {
        'apiKey': api_key,
        'format': 'json',
        'show': 'customerReviewAverage'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['products'][0]['customerReviewAverage']
    else:
        return None
    
api_key = 'wINttyWYgD90GtG41slMERbE'
sku = '16043472'  # Example SKU
review_score = get_review_score(api_key, sku)
print(f"The customer review average for SKU {sku} is: {review_score}")