import requests
re = requests.get("http://www.gomaji.com/index.php?city=Taichung&tag_id=28")
print(re.text)
