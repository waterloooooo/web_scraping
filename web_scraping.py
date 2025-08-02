import requests
from bs4 import BeautifulSoup

# Target website
url = "http://quotes.toscrape.com"

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote blocks
quotes = soup.find_all('div', class_='quote')

# Loop through and print each quote and author
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f"{text} — {author}")
