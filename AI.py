from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import os
from AD import synopsis

def photo():
    z=synopsis()
    site = 'https://www.google.com/search?tbm=isch&q='+z[0]+" anime 4k wallpapers"
    driverpth = "C:\\Program Files (x86)\\chromedriver.exe"


    #providing driver path
    driver = webdriver.Chrome(executable_path=driverpth)

    #passing site url
    driver.get(site)


    #if you just want to download 10-15 images then skip the while loop and just write
    #driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


    #below while loop scrolls the webpage 7 times(if available)


        
    try:
            #for clicking show more results button
            driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img").click()
    except Exception as e:
        pass
    time.sleep(5)
        

    #parsing
    soup = BeautifulSoup(driver.page_source, 'html.parser')


    #closing web browser
    driver.close()


    #scraping image urls with the help of image tag and class used for images
    img_tags = soup.find("div",attrs = {'class' : 'v4dQwb'})
    time.sleep(5)
    x = img_tags.find('a')
    time.sleep(5)
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
photo()
