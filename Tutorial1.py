#Tutorial taken from https://www.youtube.com/watch?v=gRLHr664tXA
#Tech with Tim Beautiful Soup 4 Tutorial #1 - Web Scraping With Python

from bs4 import BeautifulSoup
with open("index.html","r") as f:
    doc = BeautifulSoup(f,'html.parser')

#print(doc.prettify())

#tag = doc.title #access inside a tag
#tag.string = "hello" #changing the title
#print(doc)

tags = doc.find_all("p")[0]
print(tags.find_all("b"))