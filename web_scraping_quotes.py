import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/quotes/tag/inspirational"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.select('div.quoteText')

for i, q in enumerate(quotes[:5], start=1):  # Top 5 quotes
    text = q.get_text(strip=True, separator=' ').split('―')[0]
    print(f"{i}. {text}")
