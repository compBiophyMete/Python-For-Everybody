#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
_dict = dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From ') :
        line=line.split()
        _dict[line[1]] = _dict.get(line[1],0)+1
    else :
        continue
        
maxNumber = None
maxName = None
for key,value in _dict.items() :
    if maxNumber is None or value > maxNumber :
        maxNumber=value
        maxName=key
print(maxName, maxNumber)
