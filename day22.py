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





url2 = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {'User-Agent': 'Mozilla/5.0'}
response2 = requests.get(url2, headers=headers)
soup2 = BeautifulSoup(response2.content, 'html.parser')

names = soup2.find_all('span', class_ = 'fn')

print(f"Found: {len(names)} names")
print(soup2.find('table', class_= 'wikipedia'))
presidents =[]
for name in names:
    presidents.append({'name': name.text.strip()})


with open('presidents.json', 'w') as f:
    json.dump(presidents, f, indent=2)

print(f"Saved {len(presidents)} presidents to presidents.json!")