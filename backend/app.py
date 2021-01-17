import sqlite3
import json
import os
from datetime import datetime
from threading import Timer

import requests
from flask import Flask, request, send_file, redirect, url_for, jsonify

conn = sqlite3.connect(r'C:\Users\posinski\PycharmProjects\Dash\dash_project\backend\Sqlite-Data\example.db')

app = Flask(__name__)
data = ''


def update_data(interval):
    Timer(interval, update_data, [interval]).start()
    conn = sqlite3.connect('Sqlite-Data/example.db')
    for i in range(1, 7):
        res = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/{str(i)}')
        json1 = res.json()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        conn.execute(
            "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, %s)" % (
                dt_string, int(json1['trace']['sensors'][0]['value']), int(json1['trace']['sensors'][1]['value']),
                int(json1['trace']['sensors'][2]['value']), int(json1['trace']['sensors'][3]['value']),
                int(json1['trace']['sensors'][4]['value']), int(json1['trace']['sensors'][5]['value']), i))
    conn.commit()
    conn.close()


update_data(0.6)


@app.route('/get/<id>')
def get_id(id):
    connection = sqlite3.connect(r'C:\Users\posinski\PycharmProjects\Dash\dash_project\backend\Sqlite-Data\example.db')
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
    connection = sqlite3.connect(r'C:\Users\posinski\PycharmProjects\Dash\dash_project\backend\Sqlite-Data\example.db')
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


if __name__ == '__main__':
    app.run()
