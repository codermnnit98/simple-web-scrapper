import bs4
import requests
from bs4 import BeautifulSoup
import re


inp = raw_input()
print(inp)



page = requests.get("http://www.google.com/search?q=" + inp + "wikipedia")
soup = BeautifulSoup(page.content,'html.parser')
link = soup.find('h3')
str=link.a['href']

start=str.find('h')
end=str.find('&')
str=str[start:end]
#print(str)

page=requests.get(str)
soup=BeautifulSoup(page.content,'html.parser')
link=soup.find_all('tr')


born=soup.find('span',class_="bday")
par_born=born.find_parent('td')

if par_born.find('span',class_="nickname"):
	print("Nickname:"+par_born.find('span',class_="nickname").string)
else:
    print("Nickname can't be displayed, please try again")

answer =(''.join(par_born.findAll(text=True))).encode("utf-8")

print(answer)

