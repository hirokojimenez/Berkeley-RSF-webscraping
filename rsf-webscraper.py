from datetime import datetime
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# URL of the page to scrape
URL = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'
CHECK_EVERY = 15  # Check weight room status every X seconds

def get_fullness(browser):
    try:
        browser.get(URL)
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_fullness__rayxl")))
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        parent = soup.find_all('div', attrs={'class': 'styles_fullness__rayxl'})
        if len(parent) != 1:
            raise ValueError("Multiple or no fullness elements found")
        for elt in parent[0]:
            if 'Full' in elt.text:
                return int(elt.text.strip().split('%')[0])
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")

# Set up a Service object to use ChromeDriverManager
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# Start an output file
outfile = 'weightroom.csv'
with open(outfile, 'a') as f:
    while True:
        fullness = get_fullness(browser)
        if fullness is not None:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(timestamp, fullness)
            f.write(f'{timestamp},{fullness}\n')
        else:
            print("Failed to retrieve fullness data")
        f.flush()
        time.sleep(CHECK_EVERY)