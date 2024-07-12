from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

with open('corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# Preprocess and create TF-IDF index
documents = [doc['text'] for doc in corpus]
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents).toarray()

def retrieve_answer(question):
    query_vector = vectorizer.transform([question]).toarray()
    cosine_similarities = np.dot(query_vector, vectors.T).flatten()
    best_match = np.argmax(cosine_similarities)
    return documents[best_match]

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    answer = retrieve_answer(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
