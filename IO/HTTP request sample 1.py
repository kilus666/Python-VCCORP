# Test beautiful soup
from bs4 import BeautifulSoup as bts
import requests

# parse the html with lxml and beautifulsoup
# get the desire data from the html
with open('simple.html') as htmlFile:
    soup= bts(htmlFile, 'lxml')
# get the title
match = soup.title.text


# get the prefified html
prettifiedSoup = soup.prettify()


with open('simple.html') as htmlFile:
    soup= bts(htmlFile, 'lxml')
# Find the first return class named article
article = soup.find('div', class_='article')
    #print the headline 
headline= article.h2.a.text
print(headline)
    #print the summary
summary= article.p.text
print(summary)

# print the headline and summary of all article class

for i in soup.findAll("div", class_= 'article'):
    headline= article.h2.a.text
    print(headline)
    summary= article.p.text
    print(summary)
    print( )

