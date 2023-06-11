#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1798389.xml (Sum ends with 68)
#You do not need to save these files to your folder since your program will read the data directly from the URL.

#Sample Execution

#$ python3 solution.py
#Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieved 4189 characters
#Count: 50
#Sum: 2...

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location: ')
print('Retrieving ', url)
#' http://py4e-data.dr-chuck.net/comments_42.xml'
# http://py4e-data.dr-chuck.net/comments_1798389.xml
html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved ', len(html), 'characters')
tree = ET.fromstring(html)
data= tree.findall('comments/comment')
lst_numbers = []
for datum in data :
    lst_numbers.append(int(datum.find('count').text))
print('Count: ', len(lst_numbers))
print('Sum: ', sum(lst_numbers))


