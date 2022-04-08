
import csv
from operator import delitem
import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    responce = requests.get(url)
    return responce.text


def write_to_csv(data):
    with open('kivano_mobilki.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'],
                        data['price'],
                        data['photo']))



def get_total_pages(html):
    soup = bs(html, 'lxml')
    pages_ul = soup.find('div', class_='pager-wrap').find('ul')
    pages_a =pages_ul.find_all('li')[-1]
    total_pages = pages_a.find('a').get('href').split('=')[-1]
    return int(total_pages)




def get_page_data(html):
    soup = bs(html, 'lxml')
    product_list = soup.find_all('div', class_='list-view')
    
    for product in product_list:
        
        try:
            photo = product.find('a').find('img').get('src')
            
        except:
            photo = ''

        try:
            title = product.find('div', class_='listbox_title oh').find('a').text
            
        except:
            title = ''

        try:
            price = product.find('div', class_='listbox_price text-center').find('strong').text
            
        except:
            price= ''   
            
        data = {'title': title, 'price': price, 'photo': photo}
        write_to_csv(data)
         


def main():
    mobilka_url = 'https://www.kivano.kg/mobilnye-telefony'
    pages = '?page='
    total_pages = get_total_pages(get_html(mobilka_url))
    

    for page in range(1,total_pages+1):
        url_with_page = mobilka_url + pages + str(page) 
        html = get_html(url_with_page)
        get_page_data(html)

main()
