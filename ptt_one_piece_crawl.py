import json, requests, pyprind
from bs4 import BeautifulSoup

data = []

for i in pyprind.prog_bar(range(1290, 1305-1), track_time=False):
    response = requests.get('https://www.ptt.cc/bbs/ONE_PIECE/index{}.html'.format(i))
    soup = BeautifulSoup(response.text)

    for j in soup.select('.title a'):
        data.append({'title':j.text, 'url': 'https://www.ptt.cc'+j['href']})

for article in data:
    print ("name : " +article['title'])
    print ("url : " +article['url'])
