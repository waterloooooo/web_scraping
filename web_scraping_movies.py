import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Select the movie blocks
movies = soup.select('li.ipc-metadata-list-summary-item')

print("Top 10 IMDb Movies:\n")
for i, movie in enumerate(movies[:10], start=1):
    title_tag = movie.select_one('h3')
    year_tag = movie.select_one('span.sc-15ac7568-7.cCsint.cli-title-metadata-item')
    
    if title_tag:
        title = title_tag.get_text(strip=True).split('. ')[-1]  # Remove number prefix
    else:
        title = "N/A"
    
    year = year_tag.text.strip() if year_tag else "N/A"

    print(f"{i}. {title} ({year})")
