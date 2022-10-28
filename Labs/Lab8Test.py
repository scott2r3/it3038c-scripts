import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://books.toscrape.com/")

soup = BeautifulSoup(page.content, "html.parser")
content = soup.find_all(class_="product_pod")
content = str(content)

retitles = r'title="(.*?)">'
titleslist = re.findall(retitles, content)
reprices = "£(.*?)</p>"
pricelist = re.findall(reprices, content)
reinstock = ("In stock")
instocklist = re.findall(reinstock, content)

with open("output1.txt", "w") as f:
   for title, price, instock in zip(titleslist, pricelist, instocklist):
       f.write(title + "\t" + price + "\t" + instock + "\n")