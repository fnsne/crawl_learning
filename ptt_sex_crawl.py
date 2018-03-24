import json, requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ptt.cc/bbs/sex/index.html", cookies={'over18':'1'})
soup = BeautifulSoup(response.text, "lxml")
article = soup.select(".title a")[0]
#print (article)
first_article = {}
first_article['title'] = article.text
first_article['url'] = "https://www.ptt.cc/" + article['href']

response = requests.get(first_article['url'], cookies={'over18':'1'})
soup = BeautifulSoup(response.text, "lxml")

body = {}
body['title'] = soup.select("title")[0]
body['auther'] = soup.select(".article-meta-value")[0].text
body['text'] = soup.select("#main-content")[0].contents[4]
body['content'] = soup.select("#main-content")[0].text
print(body['title'])
print(body['auther'])
print(body['content'])
