import requests
from bs4 import BeautifulSoup
import pandas as pd

def ScrapeImoveis():
    productlinks = []
    aps = []
    baseurl = 'https://www.dfimoveis.com.br/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}


    for x in range(1,100):
        r = requests.get(f'https://www.dfimoveis.com.br/aluguel/df/brasilia/apartamento?pagina={x}')
        soup = BeautifulSoup(r.content, 'lxml')
        productlist = soup.find_all('li', class_ = 'property-list__item')
        for item in productlist:
            for link in item.find_all('meta',itemprop = 'url'):
                productlinks.append(baseurl + link['content'])


    def dynamic_portion(soup):
        temp_data = {}
        for item in soup.findAll('h6',class_ ='mb-0 text-normal'):
            item = item.text.split(':')
            if len(item)==2:
                key,val = map(str.strip,item)
                temp_data[key]=val
        return temp_data 

    for link in productlinks:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')
        name = soup.find_all('h1', class_ = 'mb-0 font-weight-600 fs-1-5')[0].text.strip()
        price = soup.find_all('small', class_ = 'display-5 text-warning')[2].text.strip()
        area = soup.find_all('small', class_ = 'display-5 text-warning')[0].text.replace("m²","").strip()
        valueperm2 = soup.find_all('small', class_ = 'display-5 text-warning')[1].text.strip()
        data = {'name':name,
                'link':link,
                'price':price,
                'area':area,
                'valueperm2':valueperm2
                }
        temp_data = dynamic_portion(soup)
        data.update(temp_data)
        print(data)
        aps.append(data)

    df = pd.DataFrame(aps)
    df.to_csv('../data/data.csv', encoding='utf-8')