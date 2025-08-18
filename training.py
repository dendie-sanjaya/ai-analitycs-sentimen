import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv('dataset.csv')

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['sentiment'], test_size=0.2, random_state=42
)

# Create a pipeline for the model
# Using TfidfVectorizer to convert text to numerical features
# and LogisticRegression for classification
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the trained model
joblib.dump(pipeline, 'sentiment_model.pkl')
print("Model trained and saved as sentiment_model.pkl")

# (Optional) Evaluate the model
accuracy = pipeline.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")