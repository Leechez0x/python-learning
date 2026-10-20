import requests
import json
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

articles = []

rows = soup.find_all('tr', class_ = 'athing')

for row in rows:
    title_tag = row.find('span', class_ ='titleline')
    title = title_tag.text if title_tag else "No title"

    next_row = row.find_next_sibling('tr')
    score_tag = next_row.find('span', class_='score') if next_row else None
    score = score_tag.text if score_tag else "No score"


    articles.append({'title': title, 'score': score})


for article in articles:
    print(f"{article['score']} - {article['title']}")

with open('hacker_news.json', 'w') as f:
    json.dump(articles, f, indent=2)

print("Saved to hacker_news.json!")