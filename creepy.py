import bs4
import requests
import time
import json
import numpy as np

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

def random_int(x):
      p = np.random.randint(x,size=1)
      q = str(p[0])

      return q

def url_list():
      z = random_int(105)
      url = "https://www.creepypasta.com/archive/top-ranked/?_page="+z

      response = requests.get(url)
      if response.status_code == 200:
            webpage = response.content
            final_list = []
            soup = bs4.BeautifulSoup(webpage, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True, attrs={'class' : '_self cvplbd'})]
            x = int(len(links))
            c = int(random_int(x))
            
            res = str(links[c])
            
            return res

      else:
            url_list()


def story():
      try:
            url_var = url_list()
            
            response_1 = requests.get(url_var) # opens the URL
            if response_1.status_code == 200:
                  html = response_1.content # returns the content of the page
                  final_text = []
                  soup_1 = bs4.BeautifulSoup(html, 'html.parser')
                  title = soup_1.find('h1', attrs={'class' : 'entry-title'}).text.strip()
                  info = soup_1.find_all('p')
                  for i in info:
                        final_text.append(i.text)

            
                  m = concatenate_list_data(final_text)

                  return (title, m)
            
            else:
                  story()

      except requests.Timeout as e:
            m = str(e)

            return m




