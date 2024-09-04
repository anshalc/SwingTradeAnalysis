import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options  # Use Edge options, not Chrome options

def get_driver():
    edge_options = Options()
    edge_options.add_argument("--headless")  # Run in headless mode
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")

    # Correct the webdriver to use Edge
    service = Service("/usr/local/bin/msedgedriver")  # Path to Edge WebDriver (msedgedriver)
    driver = webdriver.Edge(service=service, options=edge_options)  # Use Edge, not Chrome

    return driver

def test_driver():
    driver = get_driver()

    driver.get('https://finance.yahoo.com/quote/AAPL/')

    print("Page Titile is:", driver.title)

    driver.quit()


if __name__ == "__main__":
    test_driver()