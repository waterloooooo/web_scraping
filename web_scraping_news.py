import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Get the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Look for story titles in the correct class
stories = soup.select('tr.athing')

# Loop through and extract titles + links
for i, story in enumerate(stories[:10], start=1):
    title_tag = story.select_one('span.titleline > a')
    if title_tag:
        title = title_tag.text
        link = title_tag['href']
        print(f"{i}. {title}\n   {link}\n")
