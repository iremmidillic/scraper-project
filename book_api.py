from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    try:
        df = pd.read_csv('books.csv')
        books = df.to_dict(orient='records')
        return jsonify(books)
    except FileNotFoundError:
        return jsonify({"error": "books.csv not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
