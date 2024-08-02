from flask import Flask, request, jsonify
import data_collection

app = Flask(__name__)

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    sku = request.args.get('sku')

    bestbuy_review_score = data_collection.get_review_score(sku)

    return jsonify({
        'sku': sku,
        'bestbuy_review_score': bestbuy_review_score
    })

if __name__ == '__main__':
    app.run(debug=True)

