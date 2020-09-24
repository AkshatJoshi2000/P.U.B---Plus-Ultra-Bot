def score(TeamA, TeamB):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    import os
    import time
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = os.getcwd() +"\\chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

    driver.get("https://www.google.com")
    time.sleep(1)
    search=driver.find_element_by_xpath("//input[@name='q']")
    search.send_keys(TeamA,' vs ',TeamB)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        r_score = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[1]')
        l_score=driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]')
        out=driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[1]/div/div/div/div').text ,'-->','%s-%s'%(r_score.text, l_score.text)
        return(out[0]+out[1]+out[2])
    except NoSuchElementException:
        try:
            if   driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table') != None:
                if int(driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div/div/table/tbody/tr[3]/td[3]/div[1]/div/div[2]/span').text[5:]) >= 18:
                         print (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[1]/div/div/div/div').text + ' ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div/div/table/tbody/tr[5]/td[2]/div[1]/div').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div/div/table/tbody/tr[6]/td[2]/div[1]/div').text  + ' ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div/div/table/tbody/tr[3]/td[3]/div[1]/div/div[2]/span').text)
                else:
                    print( "No recent matches found")
                try:
                    if driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr[1]/td[2]/div/div/div/table/tbody/tr[3]/td[3]/div/div/div/div[1]') != None:
                        return 'next match is on '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr[1]/td[2]/div/div/div/table/tbody/tr[3]/td[3]/div/div/div/div[1]').text
                except NoSuchElementException:
                    return "No upcoming matches"
        except NoSuchElementException:
            return 'match is scheduled for %s' %driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[1]/div/span[2]').text
print(score('barca','real madrid'))
