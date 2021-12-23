# pip install selenium beautifulsoup4
# imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

chromedriver_path = "C:\\Users\\ytang\\Documents\\workspace\\content-moderation\\chromedriver.exe"
service = Service(chromedriver_path)
options = Options()
options.add_argument("--headless")

# function
def scrape_page_text(url: str):
    # create driver
    driver = webdriver.Chrome(service=service, options=options)

    # launch driver
    driver.get(url)
    sleep(3)
    
    # get soup from driver page
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    # scrape all the text from page
    text = soup.get_text()
    text = text.replace("\n", "")
    
    return(text)

# url = "https://pythonalgos.com/2021/11/20/web-scraping-the-easy-way-python-selenium-beautiful-soup/"

# print(scrape_page_text(url))