#!/usr/bin/python
#import os,sys,unicodedata,html2text,urllib,re
#from bs4 import BeautifulSoup
import html2text
#import urllib.request #python 3
import urllib

#=======================
# 20140130
# Retrieve text from a web site
# Count the number of character
# Required html2text 
#  [AARONSW](http://www.aaronsw.com/2002/html2text/)
#  [GitHub](https://github.com/aaronsw/html2text)
#=======================

# python3
#fulltext = urllib.request.urlopen('http://news.sabay.com.kh/') 
#python2http://docs.python.org/2/howto/unicode.html
fulltext = urllib.request.urlopen('http://news.sabay.com.kh/')

data = fulltext.read().decode('utf-8')
#print (data)
s = html2text.html2text(data)
mydict = {}
for i in range(6016, 6122): #All khmer characters
    character =chr(i)
    print (i, '\t', chr(i), '\t', s.count(chr(i)))
    mydict[chr(i)] = s.count(chr(i))
    print (mydict[chr(i)])
    
#print (mydict)
