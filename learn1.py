import requests
import json
from bs4 import BeautifulSoup

result = []


for page_num in range(1,6):
    url = f'https://quotes.toscrape.com/page/{page_num}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    quotes = soup.find_all('span', class_ ='text')
    authors = soup.find_all('small', class_ ='author')

    for i in range(len(quotes)):
        data = {
            'quote': quotes[i].text.strip('""\u201c\u201d'),
            'author': authors[i].text
        }
        result.append(data)
    print(f"page {page_num} scrapped - {len(quotes)} quotes found")

print()
print(f"Total quotes collected: {len(result)}")

# Save to a JSON file
with open('quotes.json', 'w') as f:
    json.dump(result, f, indent=2)

print("Data saved to quotes.json!")