#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1798385.txt (There are 86 values and the sum ends with 362)
#These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program
fh = open('regex_sum_1798385.txt', 'r')
nmb_lst =  []
_sum = 0
for line in fh :
    line = line.strip()
    x=re.findall('([0-9]+)', line)
    if len(x) > 0 :
        nmb_lst.extend(x)
    else :
        continue
print(nmb_lst)
for datum in nmb_lst :
    datum = float(datum)
    _sum += datum
print('Check-Number of numerical entries:', len(nmb_lst))
print('Sum:', int(_sum))
