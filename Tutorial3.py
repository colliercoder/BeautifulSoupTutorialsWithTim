#https://www.youtube.com/watch?v=lC6mucyD17k
#Beautiful Soup 4 Tutorial #3 - Navigating The HTML Tree

from bs4 import BeautifulSoup
import requests
import re

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result,'html.parser')

#tbody holds the table in the website <tbody>
tbody = doc.tbody
#trs are the rows <tr>
trs = tbody.contents
print(trs)
"""
print(trs[0].next_sibling)
print(trs[1].previous_sibling)
print(list(trs[0].next_siblings))
"""
print(trs[0].parent.name)
print(list(trs[0].contents))
print(list(trs[0].children))
print(list(trs[0].descendants))

#loop through all the table rows <trs>
prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    print(fixed_name, fixed_price)

    #putting it back in the dictionary
    prices[fixed_name] = fixed_price
    print(prices)


