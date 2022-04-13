from bs4 import BeautifulSoup
import requests

#how to get the HTML from the website

website='https://subslikescript.com/movie/Titanic-120338'
result=requests.get(website)
content=result.text

soup=BeautifulSoup(content,'lxml')
#print(soup.prettify())

#how to scrape a single page

box=soup.find('article',class_='main-article')
title=box.find('h1').get_text()

transcript=box.find('div',class_='full-script').get_text(strip=True,separator=' ')
#print(type(transcript))

#exporting data to a txt file

with open(f'{title}.txt','w',encoding="utf-8") as f:
    f.write(transcript)
