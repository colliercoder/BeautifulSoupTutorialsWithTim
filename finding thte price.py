from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)

doc = BeautifulSoup(result.text,'html.parser')
print(doc.prettify())

#looking for the dollar sign

prices = doc.find_all(text="$")
print(prices)

#need to find the parent of the dollar sign
parent = prices[0].parent

print(parent)

#the price is embedded in the strong tag

strong = parent.find("strong")
print(strong.string)