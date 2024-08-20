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

    #Fetch products data from bestbuy
    products, error = bestbuy_data_collection.get_rating(user_input)
    
    if error:
        return render_template('index.html', error=error)
    
    if not products:
        return render_template('index.html', error='No products found. Please enter a valid model.')
    
    #Fetch PCMag rating
    pcmag_rating =pcmag_data_collection.get_rating(user_input)
    
        
    product_BestBuyReview = [
        {
            'sku': product['sku'],
            'name': product['name'],
            'BestBuy_rating': product.get('customerReviewAverage', 'No rating available'),
        }
        for product in products
        
    ]

    product_PCMagReview = [
        {
            'PCMag_rating': pcmag_rating
        }
    ]

     
    return jsonify(product_BestBuyReview, product_PCMagReview)
    

if __name__ == '__main__':
    app.run(debug=True)



