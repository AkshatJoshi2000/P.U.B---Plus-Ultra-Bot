from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import bs4
import requests
import urllib.request
import time
import sys
import os
from AD import synopsis

def photo():
    z=synopsis()
    site = 'https://www.google.com/search?tbm=isch&q='+z[0]+" anime 4k wallpapers"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--headless")
    chrome_driver = "C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
    driver.get(site)

    try:
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img").click()
    except Exception as e:
        pass
    time.sleep(5)
 
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    driver.close()

    img_tags = soup.find("div",attrs = {'class' : 'v4dQwb'})
    x = img_tags.find('a')
    y = x.findAll('img')

    fin = []


    count = 1
    for i in y:
        #print(i['src'])
        if count<=1:
            #passing image urls one by one and downloading
            link = i['src']
            count+=1
        else:
            pass
    fin.append(link)
    fin.append(z[0])
    fin.append(z[1])
    return fin
