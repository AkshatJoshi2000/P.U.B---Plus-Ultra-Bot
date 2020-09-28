import bs4
import requests

def nickn():
    url = "https://www.generatormix.com/random-anime-character-generator"

    response = requests.get(url) # opens the URL
    html = response.content # returns the content of the page

    z = []

    soup = bs4.BeautifulSoup(html, 'html.parser')
    rel = soup.find('div',attrs={'class' : 'col-12 tile-block group marg-top'})
    name = rel.find('h3', attrs={'class' : 'text-center'}).text.strip()

    return name
