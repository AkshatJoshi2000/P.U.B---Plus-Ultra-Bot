def score(TeamA= 'Cricket Score', TeamB=None):
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
    if TeamA == 'Cricket Score':
        search.send_keys(TeamA)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        try: 
            teams = (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text +' vs ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text)
            score=(driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]').text +' '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div').text + ' '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/span[1]').text)
            if driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]').text == 'Yet to bat':
                overs = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]').text
            else:
                overs = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]').text
            run_rate = + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/span[2]/span[2]').text
            return (teams, score, overs, run_rate )

        except NoSuchElementException:
            #time1 is the time today's match is scheduled
            try:
                time1 = (' is scheduled at ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/span[2]').text)
                return teams, time1
            except NoSuchElementException:
                teams_= (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text +' vs ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text)
                score_=(driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div').text +' '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]').text)
                result = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div').text
                return teams_, score_, result

    else:
        search.send_keys(TeamA,' vs ',TeamB)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        r_score = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]')
        l_score=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]')
        out= '%s vs %s'%(TeamA, TeamB),'%s - %s'%(r_score.text, l_score.text), driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div').text, '-- next match is on '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div').text
        return out[0], out[1], out[2], out[3], out[4] #Teams, Score, Result, Next Match
    except NoSuchElementException:
        try:
            r_score_table = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[3]/td[2]/div[2]/div/div[1]').text
            l_score_table = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[4]/td[2]/div[2]/div/div').text
            out_2 = '%s vs %s'%(TeamA, TeamB),'%s - %s'%(r_score_table, l_score_table), driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[5]/td[1]/div/span').text, '-- next match is on '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div').text
            return out_2[0],out_2[1], out_2[2], out_2[3] #Teams, Score, Result, Next Match
            try:
                date = (' match to be held on '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[1]/div/span[2]').text)
                return('%s vs %s'%(TeamA, TeamB), date) #Teams, Date of Match
            except NoSuchElementException:
                date2= (' match to be held on '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div').text)
                return('%s vs %s'%(TeamA, TeamB), date2) #Teams, Date Of Match
print(score())
