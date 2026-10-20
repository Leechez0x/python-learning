import requests
import json
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

labels = soup.find_all('span', class_ = 'stat-label')
figures = soup.find_all('span', class_ ='stat-figure' )

for i in range(len(labels)):
    print(labels[i].text, ':', figures[i].text)

data = []
for i in range(len(labels)):
    data.append({
        'label': labels[i].text,
        'value': figures[i].text
    })

with open('bu_facts.json', 'w') as f:
    json.dump(data, f, indent = 2)


print("Saved to bu_facts.json!")

