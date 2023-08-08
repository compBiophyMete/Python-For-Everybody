#This application reads an iTunes export file in XML and produce a properly normalized database
import sqlite3
import xml.etree.ElementTree as ET
#Artist table should have a unique id and name. Id should not be null and be increased when you insert new rows.
#Genre table should have a unique id and name. Id should not be null and be increased when you insert new rows
#Album table should have unique id, non-unique artist_id, and unique title.
#Track table should have a unique id, and title, whereas album_id and genre_id can be any integer. Similar to album_id & genre_id, the table should harbor len, rating, and count which accept integer values. Id should not be null and be increased when you insert new rows
_database = sqlite3.connect('assignment2.sqlite')
curr = _database.cursor()
curr.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );

    CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );

    CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
    );

    CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
    );
''')
tree = ET.parse('Library.xml')
all_branches = tree.findall('dict/dict/dict')
#print(all_branches)

def lookup(dictionary, key):
    found = False
    for child in dictionary:
        if found :
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None
for element in all_branches:
    if (lookup(element, 'Track ID') is None) : continue
    name = lookup(element, 'Name')
    artist = lookup(element, 'Artist')
    genre = lookup(element, 'Genre')
    album = lookup(element, 'Album')
    count = lookup(element, 'Play Count')
    rating = lookup(element, 'Rating')
    length = lookup(element, 'Total time')
    if album is None or genre is None or name is None or artist is None :
        continue
    curr.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    curr.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = curr.fetchone()[0]

    curr.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    curr.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = curr.fetchone()[0]

    curr.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    curr.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = curr.fetchone()[0]

    curr.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )

    _database.commit()
