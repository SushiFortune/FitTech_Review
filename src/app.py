from flask import Flask, jsonify
import data_collection

app = Flask(__name__)

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    products = data_collection.search_fitbit_sense_2()
    if products:
        product_reviews = [
            {
                'sku': product['sku'],
                'name': product['name'],
                'rating': product.get('customerReviewAverage', 'No rating available')
            }
            for product in products
        ]
        return jsonify(product_reviews)
    else:
        return jsonify({'error': 'No products found'})

if __name__ == '__main__':
    app.run(debug=True)


