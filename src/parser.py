import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import json
from loguru import logger
from config import HEADERS, DELAY, OUTPUT_DIR
from utils import service_config
import csv

from utils import load, all_data

url_main = "https://zara-russia.ru"


def get_soup(url):
    try:
        response = requests.get(url=url, timeout=5, headers=HEADERS)
        time.sleep(DELAY)
        logger.info(f"Успешно загружена страница: {url}")
        return BeautifulSoup(response.text, "lxml")
    except Exception as e:
        logger.error(f"Ошибка загрузки {url}: {e}")
        return None


def parse_page(soup):
    collections = soup.find_all("div", class_="t959__card t959__card_25")

    collections_list = []

    for collection in collections:
        collection_dict = {
            "title": collection.h2.text.strip(),
            "url": f"{url_main}{collection.a.get('href')}",
        }

        collections_list.append(collection_dict)

    return collections_list


def save_csv(data, filename):
    keys = data[0].keys()

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    filepath = Path(OUTPUT_DIR)

    with open(filepath / filename, "w") as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def save_json(collections):
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    filepath = Path(OUTPUT_DIR)

    with open(filepath / "collections.json", "w") as file:
        json.dump(collections, file, indent=4, ensure_ascii=False)


def selenium_parse_page(url):
    driver = service_config()
    driver.get(url)
    time.sleep(2)
    counter = 0
    while True:
        try:
            load(driver=driver)
            counter += 1
            logger.info(f"Нажатие кнопки: {counter}")
        except:
            break
    return all_data



def main():
    # soup = get_soup(url_main)
    # collections = parse_page(soup)
    # data = selenium_parse_page("https://zara-russia.ru/zhenshchiny_novinki_zara")
    # save_csv(data, "novinki_zara.csv")
    data_2 = selenium_parse_page("https://zara-russia.ru/zhenshchiny_belie_zara")
    save_csv(data_2, "belie_zara.csv")
    # save_json(collections)


if __name__ == "__main__":
    main()
