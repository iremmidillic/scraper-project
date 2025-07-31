import requests
from bs4 import BeautifulSoup
import csv

books = []

# Sayfaları otomatik gez
page_number = 1
while True:
    URL = f'http://books.toscrape.com/catalogue/page-{page_number}.html'
    response = requests.get(URL)
    if response.status_code != 200:
        break  # Sayfa yoksa döngüyü bitir

    soup = BeautifulSoup(response.text, 'html.parser')
    book_items = soup.select('.product_pod')

    if not book_items:
        break  # Kitap bulunamadıysa dur

    for book in book_items:
        title = book.h3.a['title']
        price = book.select_one('.price_color').text.replace('Â', '').replace('£', '').strip()
        availability = book.select_one('.availability').text.strip()
        rating = book.select_one('p.star-rating')['class'][1]  # Rating class'ı içinden alınır
        link = 'http://books.toscrape.com/catalogue/' + book.h3.a['href']
        img_url = 'http://books.toscrape.com/' + book.select_one('img')['src'].replace('../', '')

        books.append([title, price, availability, rating, link, img_url])

    page_number += 1

# CSV'ye yaz
with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Availability', 'Rating', 'Link', 'Image URL'])
    writer.writerows(books)

print(f"✅ Scraped {len(books)} books across {page_number - 1} pages and saved to books.csv")

