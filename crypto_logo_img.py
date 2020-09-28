import requests
import bs4
import datetime

def logo(crypto):

    l = crypto.replace(" ","-")
    url = "https://coinmarketcap.com/currencies/" + l + "/"
    crypto = crypto.title()
    response = requests.get(url)
    html = response.content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    c_1 = soup.find('div', attrs={'class' : 'cmc-details-panel-header__name'})
    link = soup.find('img', attrs={'alt' : crypto})['src']
    

    return link

