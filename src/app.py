from flask import Flask, jsonify, request, render_template
import bestbuy_data_collection
import pcmag_data_collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_reviews', methods=['GET'])

def get_reviews():
    user_input = request.args.get('model_name')
    if not user_input:
        return render_template('index.html', error='Model name is required')

    #Format the user input
    model_name = bestbuy_data_collection.format_model_name(user_input)

    #Check if the model name was formatted correctly
    if model_name is None:
        return render_template('index.html', error='Invalid model name format. Please try again.')
    
    #Fetch products data from bestbuy
    products = bestbuy_data_collection.search_model(model_name)
    
    if not products:
        return render_template('index.html', error='No products found. Please enter a valid model.')
    
    #Fetch PCMag rating
    pcmag_rating = pcmag_data_collection.get_rating()

   
    product_reviews = [
        {
            'sku': product['sku'],
            'name': product['name'],
            'BestBuy_rating': product.get('customerReviewAverage', 'No rating available'),
            'PCMag_rating': pcmag_rating
        }
        for product in products
    ]

     
    return jsonify(product_reviews)
    

if __name__ == '__main__':
    app.run(debug=True)



