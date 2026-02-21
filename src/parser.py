import time, json, csv, requests
from bs4 import BeautifulSoup
from pathlib import Path
from loguru import logger
from config import DELAY, OUTPUT_DIR, service_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    filepath = Path(OUTPUT_DIR)
    try:
        # Проверяем, есть ли данные
        if not data:
            logger.warning(f"Нет данных для сохранения в {filename}")
            # Создаем файл только с заголовками
            with open(filepath / filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["title", "price", "url"])
            logger.info(f"✅ Создан пустой файл {filename} с заголовками")
            return
        
        # Проверяем, что первый элемент - словарь с нужными ключами
        if not isinstance(data[0], dict):
            logger.error(f"Неверный формат данных в {filename}")
            return
        
        # Сохраняем данные
        keys = data[0].keys()
        with open(filepath / filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        
        logger.info(f"✅ Сохранено {len(data)} записей в {filename}")
        
    except Exception as e:
        logger.error(f"❌ Ошибка при сохранении {filename}: {e}")


def save_json(collections):
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    filepath = Path(OUTPUT_DIR)

    with open(filepath / "collections.json", "w") as file:
        json.dump(collections, file, indent=4, ensure_ascii=False)


def selenium_parse_page(url):
    driver = service_config()
    driver.get(url)
    processed_count = 0
    all_data = []
    while True:
        items = driver.find_elements(By.CSS_SELECTOR, ".js-product.t-store__card.t-store__stretch-col.t-store__stretch-col_25.t-align_left.t-item")
        WebDriverWait(items, 10)
        new_items = items[processed_count:]
        if not new_items:
            break
        for item in new_items:
            item_dict = {
            "title": item.find_element(By.CSS_SELECTOR,
                ".js-store-prod-name.js-product-name.t-store__card__title.t-typography__title.t-name.t-name_xs",
                ).text.strip(),
            "url": item.find_element(By.TAG_NAME,
                "a").get_attribute("href"),
            "price": item.find_element(By.CSS_SELECTOR,
                ".js-product-price.js-store-prod-price-val.t-store__card__price-value",
                ).text.strip(),
        }
            all_data.append(item_dict)
        processed_count = len(items)

        try:
            button = driver.find_element(By.CSS_SELECTOR, ".t-btnflex__text.js-store-load-more-btn-text")
            button.click()
            WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".js-product.t-store__card.t-store__stretch-col.t-store__stretch-col_25.t-align_left.t-item")) > processed_count)
        except:
            break
    driver.quit()
    return all_data


def main():
    # soup = get_soup(url_main)
    # collections = parse_page(soup)
    # zipka = load_data()
    for url, name in zipka:
        logger.info(f"Парсинг страницы: {url}")
        start = time.time()
        data = selenium_parse_page(url)
        csv_filename = f"{name}.csv"
        save_csv(data, csv_filename)
        end = time.time()
        logger.info(f"Время выполнения: {end - start} секунд")
    
def load_data():
    with open("output/collections.json", "r") as file:
        data = json.load(file)
        urls = [item["url"] for item in data]
        names = [url.split("/")[-1] for url in urls]
        zipka = zip(urls, names)
        return zipka

if __name__ == "__main__":
    main()