from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time
from mal import Anime
from mal import AnimeSearch
from bs4 import BeautifulSoup
import requests
import urllib.request
def synopsis():
    driverpth = "C:\\Program Files (x86)\\chromedriver.exe"

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=driverpth,options=options)
    driver.get('https://www.randomanime.org/custom-list/')

    time.sleep(2)
    driver.find_element_by_xpath("/html/body/main/section/footer/button[1]").click()
    time.sleep(5)


    title = driver.find_elements_by_xpath("/html/body/main/div/div/header/div[1]/div[2]/h3/span[1]")
    for post in title:
        name = post.text
    # summary = driver.find_elements_by_xpath("/html/body/main/div/div/div/section[1]/p")
    
    # for post in summary:
    #     description = post.text
    h = 1
    soup1 = BeautifulSoup(driver.page_source, 'html.parser')
    a = soup1.find('section',attrs = {'class' : 'normal-padding-top normal-padding-bottom anime-description'})
    for j in a:
        if h<=1:
            description = a.find('p').text
        else:
            pass

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find("div",attrs = {'class' : 'anime-image-position with-background'})
    x = img_tags.find('picture')
    y = x.findAll('img')
    fin = []
    # link = y.find('srcset')
    count = 1
    for i in y:
        #print(i['src'])
        if count<=1:
            #passing image urls one by one and downloading
            link = i['src']
            count+=1
        else: 
            pass
   
    fin.append('http:'+link)
    fin.append(name)
    fin.append(description[:-10])
    return fin

synopsis()

