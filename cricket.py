def cricket_live():
      import bs4
      import requests
      import time
      import json
      import numpy as np
      url = "https://www.cricbuzz.com/cricket-match/live-scores"


      response = requests.get(url)
      
      if response.status_code == 200:
            try:
                  webpage = response.content
                  final_list = []
                  soup = bs4.BeautifulSoup(webpage, 'html.parser')
                  top_row=soup.find_all('div', attrs= {"class":"cb-mtch-lst cb-col cb-col-100 cb-tms-itm"})  
                  for match in top_row:
                        teams = match.div.h3.text[1:-2]
                        print(teams)
                        block = match.find('div', attrs = {"class":"cb-scr-wll-chvrn cb-lv-scrs-col"})
                        scores = block.find_all('div')
                        score_1 = scores[1].text+ ' : ' + scores[2].text
                        if scores[5].text[-1] == 't':
                              scores[5].text = " - Yet To Bat"
                        score_2 = scores[4].text + ' : ' + scores[5].text
                        
                        try:
                            status = block.find('div', attrs = {"class":"cb-text-live"}).text
                            res = """
                                *{}*
                                {}  {}
                                {}""".format(teams, score_1, score_2, status)
                            return(res)    
                        except:
                            status = block.find('div', attrs = {"class":"cb-text-complete"}).text
                            res = """
                                *{}*
                                {}  {}
                                {}""".format(teams, score_1, score_2, status)
                            return(res) 

            except :
                return "No Ongoing Matches"                              

