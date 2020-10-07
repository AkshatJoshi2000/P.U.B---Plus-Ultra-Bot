def football_live():
      import bs4
      import requests
      import time
      import json
      import numpy as np
      url = "https://www.livescores.com/soccer/live/"


      response = requests.get(url)
      if response.status_code == 200:
            webpage = response.content
            final_list = []
            soup = bs4.BeautifulSoup(webpage, 'html.parser')
            top_row=soup.find_all('div', attrs= {"class":"row row-tall mt4"})
            if len(top_row) > 5:
                  iterator = 5
            else:
                  iterator = len(top_row)

            for i in range(iterator):
                  titles = top_row[i].div.div.find_all('a')
                  title = titles[0].text + ' - ' + titles[1].text

                  score_min_teams = soup.find_all('div', attrs = {'class':'row-gray even'})

                  minutes = score_min_teams[i].find('div', attrs = {"class":"min"}).text

                  score = score_min_teams[i].find('div', attrs = {"class":"sco"}).text

                  teams = '%s vs %s'%(score_min_teams[i].find('div', attrs = {"class":"ply tright name"}).text, score_min_teams[i].find('div', attrs = {"class":"ply name"}).text)

                  res = """
                        {}
                        *{}*
                        {}
                        {}""".format(title, teams, score, minutes)
                  print(res)
    

football_live()
