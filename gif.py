import requests
import json
import urllib.request,urllib.parse,urllib.error
import pprint
import numpy


def Gif(x, search_term):
    apikey = "<API-KEY>"
    lmt = 20
    p = numpy.random.randint(20,size=1)
    q = p[0]
    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

    if r.status_code == 200:
        anon_id = json.loads(r.content)["anon_id"]
    else:
        anon_id = ""
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" %   
        (search_term, apikey, lmt,anon_id))
    
    z=[]

    if r.status_code == 200:
        pp = pprint.PrettyPrinter(indent=4)
        top_8gifs = json.loads(r.content) 
        for i in range(len(top_8gifs['results'])):
            
            url = top_8gifs['results'][i]['media'][0]['gif']['url']
            z.append(url)
        
    else:
        top_8gifs = None
    
    p = z[q]
    
    return p


