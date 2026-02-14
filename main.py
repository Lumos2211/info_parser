from src.parser import Parser

if __name__ == "__main__":
    # Пример использования
    parser = Parser()
    urls = [
        "https://store.playstation.com/en-tr/category/d0446d4b-dc9a-4f1e-86ec-651f099c9b29/1",
    ]
    parser.run(urls)
    