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

