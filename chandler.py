import bs4
import requests
import time
import json
from urllib.request import Request,urlopen
import numpy

def Chandler():
    url = "https://inews.co.uk/light-relief/jokes/friends-chandler-bing-funniest-quotes-jokes-one-liners-25-anniversary-341132"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    p = numpy.random.randint(30,size=1)
    q = p[0]
    webpage = urlopen(req).read()
    article_text = ''
    soup = bs4.BeautifulSoup(webpage, 'html.parser')
    title = soup.find('div',attrs = {'class' : 'article-padding article-content'})
    ol = title.findAll('p')
    z=[]
   for li in ol:
        li = li.text
        z.append(li)
    
    y = z.pop(0)
    s =z.pop(0) 
    t = z.pop(0)

    res = str(z[q])
    return res
