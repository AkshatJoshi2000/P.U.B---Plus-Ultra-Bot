import requests
import json

def Animequote():
    r = requests.get("https://animechanapi.xyz/api/quotes/random")
    x = json.loads(r.content)
    z=[]
    for i in range(len(x['data'])):
                
        url = x['data'][i]['quote']
        z.append(url)
    for i in range(len(x['data'])):
                
        url = x['data'][i]['character']
        z.append(url)
    for i in range(len(x['data'])):
                
        url = x['data'][i]['anime']
        z.append(url)
    
    res = str(str(z[0])+" - "+str(z[1]))
    
    return res
