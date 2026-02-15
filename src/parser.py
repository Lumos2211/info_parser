import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import json
from loguru import logger
from config import HEADERS, DELAY, OUTPUT_DIR
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


url_main = "https://zara-russia.ru"
        
def get_soup(url):
    try:
        response = requests.get(url=url, timeout=5, headers=HEADERS)
        time.sleep(DELAY)
        logger.info(f"Успешно загружена страница: {url}")
        return BeautifulSoup(response.text, 'lxml')
    except Exception as e:
        logger.error(f"Ошибка загрузки {url}: {e}")
        return None
    
def parse_page(soup):
    collections = soup.find_all('div', class_='t959__card t959__card_25')
    
    collections_list = []
    
    for collection in collections:
        collection_dict = {
            'title': collection.h2.text.strip(),
            'url': f'{url_main}{collection.a.get('href')}'
        }
        
        collections_list.append(collection_dict)
        
    return collections_list

def save_csv(data):
    keys = data[0].keys()
    
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    filepath = Path(OUTPUT_DIR)
    
    with open(filepath / 'data.csv', 'w') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
        
def save_json(collections):
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    filepath = Path(OUTPUT_DIR)
    
    with open(filepath / 'collections.json', 'w') as file:
        json.dump(collections, file, indent=4, ensure_ascii=False)
    
def selenium_parse_page(url):
    
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    
    elements = driver.find_elements(By.CSS_SELECTOR, '.js-product.t-store__card.t-store__stretch-col.t-store__stretch-col_25.t-align_left.t-item')
    
    elem_list = []
    
    for element in elements:
        element_dict = {
            'title': element.find_element(By.CSS_SELECTOR, '.js-store-prod-name.js-product-name.t-store__card__title.t-typography__title.t-name.t-name_xs').text.strip(),
            'url': element.find_element(By.TAG_NAME, 'a').get_attribute('href'),
            'price': element.find_element(By.CSS_SELECTOR, '.js-product-price.js-store-prod-price-val.t-store__card__price-value').text.strip()
        }
        elem_list.append(element_dict)
        
    driver.quit()
    
    return elem_list
    
def main():
    # soup = get_soup(url_main)
    # collections = parse_page(soup)
    # data = selenium_parse_page("https://zara-russia.ru/zhenshchiny_novinki_zara")
    # save_csv(data)
    # save_json(collections)

    
if __name__ == "__main__":
    main()