from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time
from mal import Anime
from mal import AnimeSearch


def synopsis():
    driverpth = "C:\\Program Files\chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = "C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
    driver.get('https://www.randomanime.org/custom-list/')

    time.sleep(2)
    driver.find_element_by_xpath("/html/body/main/section/footer/button[1]").click()
    time.sleep(5)


    title = driver.find_elements_by_xpath("/html/body/main/div/div/header/div[1]/div[2]/h3/span[1]")
    for post in title:
        name = post.text
    summary = driver.find_elements_by_xpath("/html/body/main/div/div/div/section[1]/p")
    
    for post in summary:
        description = post.text
    driver.close()
    
    z=[]
    z.append(name)
    z.append(description)
    return z
  

