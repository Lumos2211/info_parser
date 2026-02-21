from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DELAY = 2  # задержка между запросами в секундах

# # Базы данных
# DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data/parser.db')

# Пути
DATA_DIR = "data"
OUTPUT_DIR = "output"
LOG_DIR = "data/logs"

# Настройки логирования
LOG_LEVEL = "INFO"
LOG_FILE = "data/logs/parser.log"

    
def service_config():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver