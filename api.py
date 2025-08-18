from flask import Flask, jsonify, request
from calculate import calculate_sentiment

app = Flask(__name__)

@app.route('/sentiment/<int:product_id>', methods=['GET'])
def get_sentiment(product_id):
    """
    API endpoint to get sentiment analysis for a product.
    Example URL: http://127.0.0.1:5000/sentiment/1
    """
    result = calculate_sentiment(product_id)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Product not found or analysis failed"}), 404

if __name__ == '__main__':
    # Pastikan file-file berikut sudah ada sebelum menjalankan API:
    # 1. init_db.py sudah dijalankan untuk membuat sentiment.db
    # 2. training.py sudah dijalankan untuk membuat sentiment_model.pkl
    app.run(debug=True)