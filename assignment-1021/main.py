#project to read stock price of ITC using Beautiful Soup- Web Scrapping.
import requests
from bs4 import BeautifulSoup

URL = "https://www.moneycontrol.com/india/stockpricequote/diversified/itc/ITC"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")#nsecp

component = soup.find(id ="nsecp")

print(component)
print("Last Market price of ITC:", component.text)
