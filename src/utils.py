import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


all_data = []


def load(driver):
    
    elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".js-product.t-store__card.t-store__stretch-col.t-store__stretch-col_25.t-align_left.t-item",
        )

    for element in elements:
        element_dict = {
            "title": element.find_element(
                By.CSS_SELECTOR,
                ".js-store-prod-name.js-product-name.t-store__card__title.t-typography__title.t-name.t-name_xs",
            ).text.strip(),
            "url": element.find_element(By.TAG_NAME, "a").get_attribute("href"),
            "price": element.find_element(
                By.CSS_SELECTOR,
                ".js-product-price.js-store-prod-price-val.t-store__card__price-value",
            ).text.strip(),
        }
        if element_dict not in all_data:
            all_data.append(element_dict)
        
        
    button = driver.find_element(By.CSS_SELECTOR, ".t-btnflex__text.js-store-load-more-btn-text")
    button.click()
    time.sleep(2)
    
    
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