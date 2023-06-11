#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1798390.json (Sum ends with 65)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location: ')
#http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1798390.json
html = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieving ', url)
print('Retrieved ', len(html), 'characters')
data_json = json.loads(html)
print('Count', len(data_json['comments']))
_comments =  data_json['comments']
_lst_count = []
for item in _comments :
    _lst_count.append(int(item['count']))
if len(_lst_count) !=  len(data_json['comments']) :
    print('  *  Something wrong!')
else :
    print('Sum: ', sum(_lst_count))



