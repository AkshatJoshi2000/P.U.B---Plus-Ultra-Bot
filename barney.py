import bs4
import requests
import time
import json
from urllib.request import Request,urlopen
import numpy
def Barney():
    url = "https://www.scarymommy.com/barney-stinson-quotes/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    p = numpy.random.randint(20,size=1)
    q = p[0]
    webpage = urlopen(req).read()
    article_text = ''
    soup = bs4.BeautifulSoup(webpage, 'html.parser')
    title = soup.find('div',attrs = {'class' : 'entry-content'})
    ol = title.find('ol')
    z=[]
    for li in ol:
        z.append(li)

    p = str(z[q])
    b = p[4:-5]

    name = "- Barney Stinson"

    return b


