# import requests
# from bs4 import BeautifulSoup
#
# url = "https://github.com/"
#
#
# r = requests.get(url)
#
# print(r.text)
#
# soup = BeautifulSoup(r.text)
# tag = soup.header
# atb = (tag.attrs)
# print(atb["class"])


import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
print(r.text,r.status_code)
# print(r.text)


soup = BeautifulSoup(r.text, features="lxml")
print(soup.find('div'))
print(soup.find("h4",{"class":"Lenova Ideal Tab"}))