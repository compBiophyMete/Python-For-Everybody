#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')
lst_h=[]
for line in handle :
    line = line.strip()
    if line.startswith('From ') :
        line = line.split()
        _h = line[5].split(':')
        lst_h.append(_h[0])
    else:
        continue
_dct = dict()
for h in lst_h :
    _dct[h] = _dct.get(h,0) + 1
srt_dct = sorted(_dct.items())
for key,value in srt_dct : 
    print(key,value)
