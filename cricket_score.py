def score(TeamA= None, TeamB=None):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    import os
    import time
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = "C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

    driver.get("https://www.google.com")
    time.sleep(1)
    search=driver.find_element_by_xpath("//input[@name='q']")
    if TeamA == None:
        search.send_keys('Cricket Score')
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        try: 
            teams = (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text +' vs ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text)
            score="Score : " +(driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]').text +' '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div').text + ' '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/span[1]').text)
            status = "Status : " + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/span[1]').text
            if driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]').text == 'Yet to bat':
                overs = "Overs : " + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]').text
            else:
                overs = "Overs : " + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]').text
            run_rate ="Run Rate --> " +  driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/span[2]/span[2]').text
            res = """

                **{}**

                {}
                {}
                {}
                {}""".format(teams, score, overs, run_rate, status)            
            return res

        except NoSuchElementException: 
            #time1 is the time today's match is scheduled
            try:
                teams__ = (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text +' vs ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text)

                time1 = ('Match is scheduled at ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/span[2]').text)
                res = '''

                    **{}**

                    {}'''.format(teams__, time1)
                return res
            except NoSuchElementException:
                teams_= (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text +' vs ' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text)
                score_="Score : " + (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]').text +' '+ driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').text + '-' + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]').text)
                result ="Result : " + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div').text
                res = '''

                    **{}**

                    {}
                    {}'''.format(teams_, score_, result)
                return res
        except:
            res = "No ongoing matches"
        return res

    else:
        search.send_keys(TeamA,' vs ',TeamB)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        r_score = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]')
        l_score=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]')
        Teams = '%s vs %s'%(TeamA.upper(), TeamB.upper())
        f_score = '%s - %s'%(r_score.text, l_score.text)
        result =  driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div').text
        next_match = "Next Mactch is on : " + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[3]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div').text
        res = '''

            **{}**

            {}
            {}
            {}'''.format(Teams, f_score, result, next_match)
        return res

    except NoSuchElementException:
        try:
            r_score_table = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[3]/td[2]/div[2]/div/div[1]').text
            l_score_table = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[4]/td[2]/div[2]/div/div').text
            Teams = '%s vs %s'%(TeamA.upper(), TeamB.upper())
            Score = '%s - %s'%(r_score_table, l_score_table)
            Result = driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[5]/td[1]/div/span').text
            Next_Match = "Next match is on : " + driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div').text
            res = '''

                **{}**

                {}
                {}
                {}'''.format(Teams, Score, Result, Next_Match)
            return res
        except NoSuchElementException:
            try:
                date = (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[1]/div/span[2]').text)
                teams = '%s vs %s'%(TeamA.upper(), TeamB.upper())
                res = '''

                    **{}**

                    {}'''.format(teams,date)
                return res

            except NoSuchElementException:
                date2= "Next Match : " + (driver.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div').text)
                Teams = '%s vs %s'%(TeamA.upper(), TeamB.upper())
                res = '''

                    **{}**

                    {}'''.format(Teams,date2) #Teams, Date Of Match
                
                return res

# print(score())