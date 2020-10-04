from mal import Anime
from bs4 import BeautifulSoup
import numpy
import requests

def animerec():

    p = numpy.random.randint(16000,size=1)
    id = int(p[0])
    # for i in range(id,16000):
    try:
        anime = Anime(id)
        title = str(anime.title)
        titlef = title.replace(' ','_')
        titlef = titlef.replace(':','_')

        url = 'https://myanimelist.net/anime/'+str(id)+'/'+titlef+'?q=cow&cat=anime'
        get = requests.get(url)
        site = get.text
        soup = BeautifulSoup(site, 'html.parser')
        #animeimage
        img_tags = soup.find("div",attrs = {'style' : 'text-align: center;'})
        x = img_tags.find('a')
        y = x.findAll('img')
        count = 1
        fin = []
        for i in y:
            if count<=1:
                link = i['data-src']
                count+=1
            else: 
                pass

        #animesynopsis
        syn_tags= soup.find('p',attrs ={'itemprop' : 'description'}).text

        fin.append(link)
        fin.append(title)
        fin.append(syn_tags)
        return fin


    except ValueError:
        animerec()

animerec()


