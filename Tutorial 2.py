#https://www.youtube.com/watch?v=lOzyQgv71_4
#Tech with Tim Beautiful Soup 4 Tutorial #2 - Web Scraping With Python

from bs4 import BeautifulSoup
import re

with open("index2.html",'r') as f:
    doc = BeautifulSoup(f,"html.parser")
"""
tag = doc.find("option")
print(tag)

#changing attributes in the tag
tag['selected']="false"
tag['color'] = 'blue'
print(tag)

#find all the attributes of option tag
print(tag.attrs)


"""
                    #tag name   #text search            #attribute search
tags = doc.find_all(["option"], text = "Undergraduate", value="undergraduate")
print(tags)
                    #class search
tags = doc.find_all(class_ = "btn-item")
print(tags)

#regular expression to find dollar sign
tags = doc.find_all(text=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())

#same as above, just limiting results to 1 result
tags = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in tags:
    print(tag.strip())

#changing the input tags of type='text' placeholders to be "I have changed you!"
tags = doc.find_all("input",type="text")
for tag in tags:
    tag['placeholder'] = "I have changed you!"

#Writing the changes into a new doc called changed.html
with open("changed.html",'w') as file:
    file.write(str(doc))
