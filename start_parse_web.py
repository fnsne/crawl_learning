import requests
import json
from bs4 import BeautifulSoup

re = requests.get("http://www.gomaji.com/index.php?city=Taichung&tag_id=28")
soup = BeautifulSoup(re.text, "lxml")
products = []
for product in soup.select("#lb_deal3g .box-shadow2px"):
    store = product.select(".ref_name_2")[0].text
    name = product.select(".proname_3")[0].text
    price = product.select(".spe-pri")[0].text
    prod = {}
    prod["store"] = store
    prod["name"] = name
    prod["price"] = price
    products.append(prod)

json.dump(products, open('推薦產品.json', 'w'))

with open( '推薦產品.json', 'r', encoding='UTF-8') as f:
    print(json.load(f))
