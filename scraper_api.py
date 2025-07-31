from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_quotes():
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = [quote.text.strip() for quote in soup.find_all('span', class_='text')]
    return jsonify(quotes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
