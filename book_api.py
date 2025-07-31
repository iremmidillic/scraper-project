from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_books():
    url = 'http://books.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.select_one('.price_color').text
        availability = book.select_one('.availability').text.strip()
        books.append({
            'title': title,
            'price': price,
            'availability': availability
        })

    return jsonify(books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
