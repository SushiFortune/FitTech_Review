from flask import Flask, jsonify, request, render_template
import data_collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    user_input = request.args.get('model_name')
    if not user_input:
        return render_template('index.html', error='Model name is required')

    # Use the format_model_name function to format the user input
    model_name = data_collection.format_model_name(user_input)

    # Check if the model name was formatted correctly
    if model_name is None:
        return render_template('index.html', error='Invalid model name format. Please try again.')

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
        return render_template('index.html', error='No products found. Please enter a valid model.')

if __name__ == '__main__':
    app.run(debug=True)



