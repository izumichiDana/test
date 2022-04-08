

import requests
from bs4 import BeautifulSoup
import csv
base_url = "https://vesti.kg"



def get_soup(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_title(url):
    db = []
    title_names = get_soup(url)
    title = title_names.find_all('div', {'class':'itemBody'})
    for x in title:
        db.append(
            {
            "name of the title": x.find('a').get_text(strip=True)
            }
        )
         
    return db
        

def write_to_csv():
    db = get_title(base_url)
    with open('novosti.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['title'])
        for x in db:

            writer.writerow([x['name of the title']])
write_to_csv()


        

# print(get_title(base_url))




