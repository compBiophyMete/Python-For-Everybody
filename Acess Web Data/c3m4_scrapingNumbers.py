#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1798387.html (Sum ends with 14)
#You do not need to save these files to your folder since your program will read the data directly from the URL.
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter -')
#http://py4e-data.dr-chuck.net/comments_42.html
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
values = list()

for tag in tags :
    values.append(int(tag.contents[0]))
print('Count ',len(values))
print('Sum ',sum(values))
