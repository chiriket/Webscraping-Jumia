from bs4 import BeautifulSoup
import requests
from lxml import html 
import json

url =('https://www.jumia.co.ke/phones-tablets/')
# soup = BeautifulSoup(url.content, "lmxl")
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "lxml")




print (content)
# print(soup.prettify())

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify()) 