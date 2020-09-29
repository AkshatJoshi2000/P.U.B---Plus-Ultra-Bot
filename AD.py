from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time
from mal import Anime
from mal import AnimeSearch
def synopsis():
    driverpth = "C:\\Program Files (x86)\\chromedriver.exe"

    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(executable_path=driverpth,options=options)
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
  

