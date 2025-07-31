🕸️ Web Scraper Collection – Quotes & Books

This project includes two Python-based web scrapers:
- 📜 **Quote Scraper**: Extracts inspirational quotes from [quotes.toscrape.com](https://quotes.toscrape.com)
- 📚 **Book Scraper**: Collects book data (title, price, rating) from [books.toscrape.com](https://books.toscrape.com)

Each scraper saves data into a .csv file and includes a basic Flask API for local access. Docker support is included.

🔧 Technologies Used
- Python 3
- BeautifulSoup4
- Requests
- Flask (for APIs)
- Docker (optional)
- CSV module

📜 Quote Scraper

📁 How It Works
1. Sends a GET request to https://quotes.toscrape.com.
2. Parses the HTML using BeautifulSoup.
3. Extracts quotes from <span class="text">.
4. Saves them into quotes.csv.

🖥️ How To Run

python scraper.py

📚 Book Scraper
📁 How It Works
Sends GET requests through all paginated book pages at https://books.toscrape.com.

Extracts: Title, Price, Availability, Rating

Saves them into books.csv.

🖥️ How To Run

python book-scraper.py

🧪 API Endpoints (Flask)
Each scraper also has its own API:

📜 Quote API

python scraper_api.py
GET /quotes: Returns all quotes in JSON

📚 Book API

python book_api.py
GET /books: Returns all books in JSON

🐳 Docker Support
You can build and run each scraper's API using Docker.

Example: Book Scraper

docker build -t book-api .
docker run -p 8080:8080 book-api
Then visit: http://localhost:8080/books

📦 Sample Output
CSV files will be generated as:

quotes.csv
books.csv
  