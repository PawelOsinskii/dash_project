# This Python file uses the following encoding: utf-8
import psycopg2 as psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname='postgres',
      user='postgres', host='db',
      password='python123')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS data_from_tesla')
c.execute('DROP TABLE IF EXISTS person')

c.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier('pythonlab'))
    )

c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname varchar(250) NOT NULL, lastname varchar(250) NOT NULL, birthdate varchar(250) NOT NULL)
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
          (id, firstname, lastname, birthdate) VALUES (1, 'Janek', 'Grzegorczyk', '1982')
          ''')
c.execute('''
          Insert into person
          (id, firstname, lastname, birthdate) VALUES (2, 'Janek', 'Grzegorczyk', '1982')
          ''')
c.execute('''
          Insert into person
          (id, firstname, lastname, birthdate) VALUES (3, 'Janek', 'Grzegorczyk', '1982')
          ''')
c.execute('''
          Insert into person
          (id, firstname, lastname, birthdate) VALUES (4, 'Janek', 'Grzegorczyk', '1982')
          ''')
c.execute('''
          Insert into person
          (id, firstname, lastname, birthdate) VALUES (5, 'Janek', 'Grzegorczyk', '1982')
          ''')
c.execute('''
          Insert into person
          (id, firstname, lastname, birthdate) VALUES (6, 'Janek', 'Grzegorczyk', '1982')
          ''')

c.close()

conn.commit()
conn.close()

print('WYKONANO')