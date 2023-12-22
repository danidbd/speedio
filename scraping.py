
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from pymongo import MongoClient
import json

def obtendo_dados():
    url = "https://www.similarweb.com/pt/top-websites/"

    option = Options()
    option.headless = True
    driver = webdriver.Chrome(options=option)

    driver.get(url)

    element = driver.find_element("xpath", "//div[@class='top-table__container']//table")
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    df_full = pd.read_html(str(table))[0]
    driver.quit()
    print("dados obtidos")
    return df_full


