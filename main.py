from src.parser import Parser

if __name__ == "__main__":
    # Пример использования
    parser = Parser()
    urls = []
    for i in range(1, 10):  # Парсим первые 2 страницы
        urls.append(f"https://store.playstation.com/en-tr/category/d0446d4b-dc9a-4f1e-86ec-651f099c9b29/{i}?10000-11999=webBasePrice&12000-*=webBasePrice")
    parser.run(urls)
    