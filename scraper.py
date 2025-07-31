import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("span", class_="text")
for i, quote in enumerate(quotes, start=1):
    print(f"{i}: {quote.text}")
    import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Quote"])

    for i, quote in enumerate(quotes, start=1):
        quote_text = quote.text.strip()
        print(f"{i}: {quote_text}")
        writer.writerow([i, quote_text])
import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'quotes.csv')
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])

    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text.strip()
        writer.writerow([text, author])
        
import csv
import os
os.makedirs("output", exist_ok=True)
output_path = "output/quotes.csv"
quotes = [
    {"quote": "The world as we have created it is a process of our thinking."},
    {"quote": "It is our choices, Harry, that show what we truly are."},
]
with open(output_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["quote"])
    writer.writeheader()
    writer.writerows(quotes)

print("Quotes written to", output_path)


