from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the corpus
with open('corpus.json', 'r') as f:
    corpus = json.load(f)

# Preprocess the corpus and create an index (For simplicity, this is just a placeholder)
index = {doc['id']: doc for doc in corpus}

def retrieve_answer(question):
    # Implement a basic IR technique (e.g., keyword matching) to retrieve the answer
    for doc_id, doc in index.items():
        if question.lower() in doc['text'].lower():
            return doc['text']
    return "Answer not found."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    answer = retrieve_answer(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
