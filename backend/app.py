import sqlite3
import json
import os
from datetime import datetime
import datetime
from threading import Timer

import requests
from flask import Flask, request, send_file, redirect, url_for, jsonify

app = Flask(__name__)
data = ''


def update_data(interval):
    Timer(interval, update_data, [interval]).start()
    conn = sqlite3.connect('Sqlite-Data/example.db')
    for i in range(1, 7):
        res = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/{str(i)}')
        json1 = res.json()
        dt_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        dt_ten_minutes = datetime.datetime.now() - datetime.timedelta(0,600)
        str_dt_ten_minutes = dt_ten_minutes.strftime("%Y-%m-%d %H:%M:%S.%f")
        conn.execute(
            "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, %s)" % (
                dt_string, int(json1['trace']['sensors'][0]['value']), int(json1['trace']['sensors'][1]['value']),
                int(json1['trace']['sensors'][2]['value']), int(json1['trace']['sensors'][3]['value']),
                int(json1['trace']['sensors'][4]['value']), int(json1['trace']['sensors'][5]['value']), i))

    conn.execute("DELETE FROM data_from_tesla where date_of_measurmenet < ?", (str_dt_ten_minutes,))
    conn.commit()
    conn.close()


update_data(0.6)


@app.route('/get/<id>')
def get_id(id):
    connection = sqlite3.connect(r'Sqlite-Data/example.db')
    cur = connection.cursor()
    cur.execute("SELECT * FROM data_from_tesla where person_id = ?", (id,))
    rows = cur.fetchall()
    json_return = []
    for row in rows:
        row_to_json = {
            'date': row[1],
            'l0': row[2],
            'l1': row[3],
            'l2': row[4],
            'p0': row[5],
            'p1': row[6],
            'p2': row[7],
            'person_id': row[8]
        }
        json_return.append(row_to_json)

    connection.close()

    return jsonify(json_return)


@app.route('/get/all')
def get_all():
    connection = sqlite3.connect(r'Sqlite-Data/example.db')
    cur = connection.cursor()
    cur.execute("SELECT * FROM data_from_tesla")
    rows = cur.fetchall()
    json_return = []
    for row in rows:
        row_to_json ={
                      'date': row[1],
                      'l0': row[2],
                      'l1': row[3],
                      'l2': row[4],
                      'p0': row[5],
                      'p1': row[6],
                      'p2': row[7],
                      'person_id': row[8]
                      }
        json_return.append(row_to_json)

    connection.close()

    return jsonify(json_return)

@app.route('/patients')
def get_all_patients():
    connection = sqlite3.connect(r'Sqlite-Data/example.db')
    cur = connection.cursor()
    cur.execute("SELECT * FROM person")
    rows = cur.fetchall()
    json_return = []
    for row in rows:
        row_to_json ={
                      'birthdate': row[4],
                      'firstname': row[2],
                      'lastname': row[3],
                      'disabled': row[1],
                      }
        json_return.append(row_to_json)

    connection.close()

    return jsonify(json_return)

@app.route('/patients/<id>')
def get_patient(id):
    connection = sqlite3.connect(r'Sqlite-Data/example.db')
    cur = connection.cursor()
    cur.execute("SELECT * FROM person where id=?", (id,))
    rows = cur.fetchall()
    json_return = []
    for row in rows:
        row_to_json = {
            'birthdate': row[4],
            'firstname': row[2],
            'lastname': row[3],
            'disabled': row[1],
        }
        json_return.append(row_to_json)

    connection.close()

    return jsonify(json_return)


if __name__ == '__main__':
    app.run()
