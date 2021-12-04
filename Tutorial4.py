#https://www.youtube.com/watch?v=zAEfWiC_KBU
#Beautiful Soup 4 Tutorial #4 - Finding The Best GPU Prices

#Find the cheapest instock product on newegg.com

from bs4 import BeautifulSoup
import requests
import re

#gpu = input("What product do you want to search for? ")
url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page,"html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = str
pages = str(page_text).split("/")[-2]
pages = int(str(pages).split(">")[-1][0:-1])

for page in range(1,pages + 1):
    #adding &page={page}
    url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

