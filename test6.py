#!/usr/bin/python
#import os,sys,unicodedata,html2text,urllib,re
#from bs4 import BeautifulSoup
import html2text
#import urllib.request #python 3
import urllib
import numpy as np
import matplotlib.pyplot as plt

#=======================
# 20140130
# Retrieve text from a web site
# Count the number of character
# Required html2text 
#  [AARONSW](http://www.aaronsw.com/2002/html2text/)
#  [GitHub](https://github.com/aaronsw/html2text)
#=======================
# TO DO
# - Save in array
# - Statistics
# - Deduction
#=======================

# python3
#fulltext = urllib.request.urlopen('http://news.sabay.com.kh/') 

#python2
fulltext = urllib.urlopen('http://news.sabay.com.kh/')

data = fulltext.read().decode('utf-8')
#print (data)
s = html2text.html2text(data)
mydict = {}

#for i in range(6016, 6122): #All khmer characters
#    character =unichr(i)
#    print i, '\t', unichr(i), '\t', s.count(unichr(i))
#    mydict[unichr(i)] = s.count(unichr(i))
#    print mydict[unichr(i)]
    
#print (mydict)


#x = np.arange(0, 10, 0.1);
#y = np.sin(x);
#plt.plot(x, y);

x = np.arange(6016, 6122)
y = np.zeros(len(x))
print len(y)

for i in range(6016,6122):
    index = i - 6016
#    print i
#    print index
    y[index] = s.count(unichr(i))
#print y
plt.plot(x,y);
plt.xlim(6016,6122);
plt.xlabel('Char id')
plt.ylabel('Count')
plt.title(r'Number of characters')
plt.show();
    

