HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

TIMEOUT = 10
RETRIES = 3
DELAY = 1  # задержка между запросами в секундах

# # Базы данных
# DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data/parser.db')

# Пути
DATA_DIR = 'data'
OUTPUT_DIR = 'output'
LOG_DIR = 'data/logs'

# Настройки логирования
LOG_LEVEL = 'INFO'
LOG_FILE = 'data/logs/parser.log'