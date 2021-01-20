# This Python file uses the following encoding: utf-8
import sqlite3

conn = sqlite3.connect(r'../Sqlite-Data/example.db')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS data_from_tesla')
c.execute('DROP TABLE IF EXISTS person')

c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY AUTOINCREMENT,  disable INTEGER, firstname varchar(250) NOT NULL, lastname varchar(250) NOT NULL, birthdate varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE data_from_tesla
          (id INTEGER PRIMARY KEY AUTOINCREMENT, date_of_measurmenet varchar(250), 
           l1 INTEGER NOT NULL,l2 INTEGER(250) NOT NULL,l3 INTEGER NOT NULL,r1 INTEGER NOT NULL,
           r2 INTEGER NOT NULL,r3 INTEGER NOT NULL,
            person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES person(id))
          ''')
c.execute('''
          Insert into person
          (id, disable, firstname, lastname, birthdate) VALUES (1, 0, 'Janek', 'Grzegorczyk', '1982')
          ''')
c.execute('''
          Insert into person
          (id, disable, firstname, lastname, birthdate) VALUES (2, 1, 'Elżbieta', 'Kochalska', '1976')
          ''')
c.execute('''
          Insert into person
          (id, disable, firstname, lastname, birthdate) VALUES (3, 0, 'Albert', 'Lisowski', '1991')
          ''')
c.execute('''
          Insert into person
          (id, disable, firstname, lastname, birthdate) VALUES (4, 1, 'Ewelina', 'Nosowska', '1998')
          ''')
c.execute('''
          Insert into person
          (id,  disable, firstname, lastname, birthdate) VALUES (5, 0, 'Piotr', 'Fokalski', '1985')
          ''')
c.execute('''
          Insert into person
          (id, disable, firstname, lastname, birthdate) VALUES (6, 0,  'Bartosz', 'Moskalski', '1981')
          ''')

conn.commit()
conn.close()