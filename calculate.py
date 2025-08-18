import sqlite3
import joblib

def calculate_sentiment(product_id):
    """
    Calculates sentiment for a given product ID.
    Returns product information and sentiment counts.
    """
    try:
        
        print(f"Calculating sentiment for product ID: {product_id}")    
        # Load the trained model
        model = joblib.load('sentiment_model.pkl')

        # Connect to the database
        conn = sqlite3.connect('product_comments.db')
        cursor = conn.cursor()

        # Get product info
        cursor.execute("SELECT id, name, price, weight FROM products WHERE id = ?", (product_id,))
        product_info = cursor.fetchone()
        if not product_info:
            return None

        product = {
            "id": product_info[0],
            "name": product_info[1],
            "price": product_info[2],
            "weight": product_info[3]
        }

        # Get comments for the product
        cursor.execute("SELECT comment FROM comments WHERE product_id = ?", (product_id,))
        comments = [row[0] for row in cursor.fetchall()]
        
        conn.close()

        if not comments:
            return {
                "product": product,
                "total_comments": 0,
                "sentiment_counts": {"positive": 0, "neutral": 0, "negative": 0}
            }

        # Predict sentiment for each comment
        sentiments = model.predict(comments)

        # Count the sentiments
        sentiment_counts = {
            "positive": sum(1 for s in sentiments if s == 'positive'),
            "neutral": sum(1 for s in sentiments if s == 'netral'),
            "negative": sum(1 for s in sentiments if s == 'negatif')
        }
        
        return {
            "product": product,
            "total_comments": len(comments),
            "sentiment_counts": sentiment_counts
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    # Example usage
    product_id_to_analyze = 1
    result = calculate_sentiment(product_id_to_analyze)
    if result:
        print(f"Sentiment analysis for Product ID {product_id_to_analyze}:")
        print(f"Product Info: {result['product']}")
        print(f"Total Comments: {result['total_comments']}")
        print(f"Sentiment Counts: {result['sentiment_counts']}")
    else:
        print("Product not found or an error occurred.")