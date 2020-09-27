import imdb
import bs4
import requests

ia = imdb.IMDb() 

def mov(req):  
    search = ia.search_movie(req)[0]
    id = search.movieID 
    series = ia.get_movie(id) 
    url = "https://www.imdb.com/title/tt" + id + "/?ref_=fn_al_tt_1"
    z = []
    response = requests.get(url)
    html = response.content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    rel = soup.find('div', attrs={'class' : 'summary_text'}).text
    new_title = str(req.title()) + "Poster"
    
    rel = rel[20:-13]

    rating = soup.find('span', attrs = {'itemprop' : 'ratingValue'}).text

    cast_1 = series['cast'][0]
    cast_2 = series['cast'][1]
    cast_3 = series['cast'][2]
    cast_4 = series['cast'][3]
    
    rel_date = soup.find('a', attrs={'title' : 'See more release dates'}).text

    path_img = soup.find('div', attrs={'class' : 'poster'})
    src_img = path_img.find('img', src = True)['src']
  
    return rel_date, src_img, rel, rating, cast_1, cast_2, cast_3, cast_4
