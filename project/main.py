import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--proxy-server=proxy")

driver = webdriver.Chrome()
driver.get("https://sbermarket.ru/")
print('Ok')
page = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located(
            (By.XPATH, 
            '//*[@id="by_courier"]/div[1]/div[2]/div[1]/div/div/input')
        )
    ).click()
time.sleep(3)
assert page
page.send_keys("Алексеевская,30, Москва")
time.sleep(2)
page.send_keys(Keys.ENTER)


#
#//*[@id="__next"]/div/div[2]/div[2]/div/div/div[3]/div/form/header/figure
#//*[@id="__next"]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/button/div
    
    
#if __name__ =="__main__":
    

#Требуется получить следующие данные:

#Адрес магазина
#Категория товара
#url товара (при наличии)
#Наименование товара
#Ссылка на изображение товара (маленькая картинка на странице категории)
#Ссылка на изображение товара (большая картинка на странице товара, если возможно получить на странице категории, без открытия страницы товара)
#Цена
#Цена без учета скидки, до применения акций, дисконтных карт и т.д. (при наличии)