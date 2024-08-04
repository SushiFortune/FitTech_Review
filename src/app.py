from flask import Flask, jsonify, request, render_template
import data_collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    model_name = request.args.get('model_name')
    if not model_name:
        return jsonify({'error': 'Model name is required'}), 400

    products = data_collection.search_model(model_name)
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



