import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import json
from loguru import logger
from src.config import HEADERS, DELAY, OUTPUT_DIR

class Parser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        
    def fetch_page(self, url):
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            time.sleep(DELAY)
            return response.text
        except Exception as e:
            logger.error(f"Ошибка загрузки {url}: {e}")
            return None
        
    def parse_page(self, url):
        html = self.fetch_page(url)
        if not html:
            return None
        soup = BeautifulSoup(html, 'html.parser')
        
        game_tile = soup.find_all(attrs={'data-qa': lambda x: x and 'productTile' in x})
        
        games = []
        
        for title in game_tile:
            
            game_data = {}
            
            name = title.find("span", class_="psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2")
            game_data['name'] = name.text.strip() if name else None
            
            price = title.find("span", class_="psw-m-r-3")
            game_data['price'] = price.text.strip() if price else None
            
            if not game_data['name']:
                continue
            
            # Проверка на дубликаты (по названию)
            if game_data['name'] in [game['name'] for game in games]:
                continue
            
            # Добавляем игру
            games.append(game_data)
            
        return games

    
    
    def save_data(self, data, filename):
        Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
        
        filepath = Path(OUTPUT_DIR) / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Сохранено {len(data)} записей в {filepath}")
    
    def run(self, urls):
        """Основной метод парсинга"""
        results = []
        for url in urls:
            logger.info(f"Парсинг {url}")
            data = self.parse_page(url)
            if data:
                results.extend(data)
            else:
                logger.warning(f"Не удалось спарсить {url}")
        
        if results:
            self.save_data(results, 'parsed_data.json')
        else:
            logger.warning("Нет данных для сохранения")
        
        return results
    