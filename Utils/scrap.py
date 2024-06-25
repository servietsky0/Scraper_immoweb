import requests
from bs4 import BeautifulSoup as bs
import regex as re
import csv

class Scraper:
    def __init__(self, ) -> None:
        pass


def price() -> str:
    url = 'https://www.immoweb.be/en/classified/house/for-sale/mechelen/2800/11486576'
    
    headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = bs(response.content, 'html.parser')

    price = soup.find('span', class_='sr-only').text

    return price


def get_link() -> str:
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance'
    
    headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = bs(response.content, 'html.parser')
    link = soup.find('a', class_="card__title-link")

    return link['href']


def get_code() -> int:
    pattern = r"[0-9]{4}"
    
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance'
    
    headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)  
    soup = bs(response.content, 'html.parser')
    code = soup.find('p', class_="card__information--locality").text
    
    code_num = re.search(pattern, code)    
    
    return code_num.group(0)


with open('data_set.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Locality', 'Type of property', 'Subtype of property', 'Price', 'Type of sale', 'Number of rooms', 'Living Area (m²)', 'Fully equipped kitchen', 'Furnished', 'Open fire', 'Terrace', 'Garden', 'Surface of the plot (m²)', 'Number of facades', 'Swimming pool', 'State of the building'])
        

#  ***********************
#  ** window.classified **
#  ***********************
