import requests

def api_call_funct ():
    url = ('https://newsapi.org/v2/everything?'
            'sources=bbc-news&'
            'from-parameter=2009-01-01&'
            'to=2018-12-31&'
           'apiKey=b059574d636640fbae75672db299911f')
    response = requests.get(url).json()
    articles = response['articles']
    titles = []
    for article in articles:
        titles.append(article['title'])
    return titles[:2]
