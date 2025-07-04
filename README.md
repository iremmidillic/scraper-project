# Web Scraper - Quote Extractor
This project is a basic Python web scraper that extracts quotes from [https://quotes.toscrape.com](https://quotes.toscrape.com) and saves them into a CSV file.
## 🔧 Technologies Used
- Python 3
- BeautifulSoup4
- Requests
- CSV module
## 📁 How It Works

1. Sends a GET request to `https://quotes.toscrape.com`.
2. Parses the HTML using BeautifulSoup.
3. Extracts all the quotes (in `<span class="text">` tags).
4. Saves the extracted data into `quotes.csv`.
## 🖥️ How To Run It

1. Clone the repository or download the project folder.
2. Open a terminal inside the folder.
3. Install dependencies:
4. Run the scraper:

```bash
python scaper.py