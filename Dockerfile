FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install beautifulsoup4 requests

CMD ["python", "scraper.py"]

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask requests beautifulsoup4

EXPOSE 8080

CMD ["python", "scraper_api.py"]

FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install requests beautifulsoup4

CMD ["python", "book-scraper.py"]

