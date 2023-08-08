#This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
import sqlite3
#Open a database file
counts = sqlite3.connect('OrganizationEmail.sqlite')
#Create a cursor to handle the database file
cur = counts.cursor()
#Check if the table exists
cur.execute('''DROP TABLE IF EXISTS Counts''')
#Create a table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
_lstInfo = []
_lstOrg = []
_dct = dict()
_file = open('mbox.txt')
for line in _file :
    if line.startswith('From ') :
        line = line.split()
        _lstInfo.append(str(line[1]))

for line in _lstInfo :
    line = line.split('@')
    _lstOrg.append(line[1])
for datum in _lstOrg :
    _dct[datum] = _dct.get(datum,0) + 1
    args = datum
    #print(args)
    cur.execute('SELECT count FROM Counts where org = ?', (args,))
    row = cur.fetchone()
    if row is None :
        cur.execute('''INSERT INTO Counts (org, count)
            VALUES (?, 1)''', (args,))
    else :
        cur.execute('UPDATE Counts SET count = count+1 where org=?', (args,))
counts.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr) :
    #row subzero is org, row subone is count
    print(str(row[0]), row[1])

###CHECK
print(sorted([(value,key) for (key,value) in _dct.items()], reverse=True))


