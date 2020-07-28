# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 03:17:44 2020

@author: BKD-pc
"""
import re
import requests
from bs4 import BeautifulSoup
import urllib.request
result=requests.get("https://www.jnu.ac.in/iha_admin")
print(result.status_code)
#status code 200 means it is accesible

src=result.content

#We need to create a Beautiful Soup object first
soup=BeautifulSoup(src,'lxml')
links=soup.find_all("a")
#print("\n")
'''
for link in links:
    if "style" in link.text:
        print(link)
        print(link.attrs['href'])
#print(links)
        '''
        
source=urllib.request.urlopen("https://www.jnu.ac.in/iha_admin").read()
#print(source)
sou=BeautifulSoup(source,'lxml')
#If we compare to print source with sou the sou will print systematically
#print(sou.find_all("p"))
info=[]

for paragraph in sou.find_all('p'):
    info.append(paragraph.string)
    #print(paragraph.string)
    #print('\n\n')

for url in sou.find_all('a'):
    print(url.get('href'))
#info=sou.get_text()
#print(info)


#The aboce code will help us to extract the email, phone number and Date
'''
emailExtract=re.findall(r'\S+@\S+',str(info)) 
lst=re.findall(r'\+\d\d\d\d\d\d\d\d\d\d\d\d+',str(info))
lst2=re.findall(r'\s\d\d\d\d\d\d\d\d\d\d+',str(info))
lst.append(lst2)
date=re.findall(r'\d{2}\/[0-9]{2}\/[0-9]{4}',str(info))
dat2=re.findall(r'\d{2}\s[A-Za-z][A-Za-z][A-Za-z]\s\d{4}',str(info))
date.append(dat2)
#mob_no_database=lst.search(lst)
print(lst)
print(emailExtract)
print(date)
'''