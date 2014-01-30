#!/usr/bin/python3
#import os,sys,unicodedata,html2text,urllib,re
#from bs4 import BeautifulSoup
import html2text, urllib.request

#=======================
# 20140130
# Retrieve text from a web site
# Count the number of character
# Required html2text 
#  [AARONSW](http://www.aaronsw.com/2002/html2text/)
#  [GitHub](https://github.com/aaronsw/html2text)
#=======================

# html_doc = ...
# soup = BeautifulSoup(html_doc)
# soup = BeautifulSoup(open("index.html"))
#soup = BeautifulSoup(open("http://news.sabay.com.kh/"))
#print(soup.get_text())


fulltext = urllib.request.urlopen('http://news.sabay.com.kh/')
data = fulltext.read().decode('utf-8')
#print (data)
s = html2text.html2text(data)
for i in range(6016, 6122): #All khmer characters
    character =chr(i)
    print (i, '\t', chr(i), '\t', s.count(chr(i)))
