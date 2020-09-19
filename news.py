import requests
import datetime

def everything_news(req):
    now = datetime.datetime.now()
    a = str(now.year)
    b = str(now.month)
    c = str(now.day-1)
    p = str(a+"-"+b+"-"+c)
    url = ('https://newsapi.org/v2/everything?'
                            'q='+req+
                            '&from='+p+
                            '&sortBy=popularity&'
                            'apiKey=<API KEY>)
    response = requests.get(url)
    z = response.json()
    H1 =  z['articles'][0]['title']
    H2 =  z['articles'][1]['title']
    H3 =  z['articles'][2]['title']
    H4 =  z['articles'][3]['title']
    H5 =  z['articles'][4]['title']
    answer = """
    1. {}
    2. {}
    3. {}
    4. {}
    5. {}""".format(H1,H2,H3,H4,H5)

    return answer
