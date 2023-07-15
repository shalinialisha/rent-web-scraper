from bs4 import BeautifulSoup
import requests

url = "https://www.padmapper.com/apartments/nashville-tn/under-1000"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

addyList = doc.find_all("a", class_= "ListItemMobile_address__16cXF")
priceList = doc.find_all("div", class_="ListItemMobile_text__3KFu_")

places = {}

for info, cost in zip(addyList, priceList):
    addy = info.get_text(strip=True)

    href = info.get('href')
    href = url + href

    price = cost.get_text(strip=True)

    places[price] = [addy, href]
    


print(places)

