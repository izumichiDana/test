import csv
import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    responce = requests.get(url)
    return responce.text


def write_to_csv(data):
    with open('moshinki.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'],
                        data['price'],
                        data['photo']))


def get_total_pages(html):
    soup = bs(html, 'lxml')
    pages_ul = soup.find('ul', class_='pagination')
    pages_a =pages_ul.find_all('li')[-1]
    total_pages = pages_a.find('a').get('href').split('=')[-1]
    return int(total_pages)


def get_page_data(html):
    soup = bs(html, 'lxml')
    product_list = soup.find_all('div', class_='list-item')
    
    for product in product_list:
        
        try:
            photo = product.find('a').get('href').strip(' ')

            
        except:
            photo =''

        try:
            title = product.find('div', class_='block title').find('h2').text.replace('\n', ' ').strip(' ')
            
        except:
            title =''

        try:
            price = product.find('div', class_='block price').find('strong').text.replace('\n', ' ').strip(' ')
            
        except:
            price=''   
            
        data = {'title': title, 'price': price, 'photo': photo}
        print(data)
        write_to_csv(data)
         

def main():
    open("moshinki.csv", 'w').close()
    mobilka_url = 'https://www.mashina.kg/search/all'
    pages = '?page='
    total_pages = get_total_pages(get_html(mobilka_url))
    

    for page in range(1,total_pages+1):
        url_with_page = mobilka_url + pages + str(page) 
        print(url_with_page)
        html = get_html(url_with_page)
        get_page_data(html)

main()