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
    
def football_h2h(TeamA, TeamB):
    TeamA = TeamA.replace(' ', '-')
    TeamB = TeamB.replace(' ', '-')
    import bs4

    import requests
    import time
    import json
    import numpy as np
    url = "https://www.fctables.com/h2h/%s/%s/"%(TeamA, TeamB)

    response = requests.get(url)
    if response.status_code == 200:
        webpage = response.content
        final_list = []
        soup = bs4.BeautifulSoup(webpage, 'html.parser')
        top_row=soup.find('div', attrs= {"class":"game_name"})    
        team_a = top_row.div.a.span.text
        team_b = top_row.find('div', attrs = {"class":"gnbox away"}).a.span.text
        scores_main = soup.find('div', attrs= {"class":"score"})
        score = scores_main.ul.li.h3.text
        date_time = scores_main.ul.li.p.text[:-6]
        teams = '%s vs %s'%(team_a, team_b)
        res="""
            *{}*
            {}
            {}""".format(teams, score, date_time)
        return(res)
football_live()
