import sqlite3
import json
import os
from datetime import datetime
from threading import Timer

import requests
from flask import Flask, request, send_file, redirect, url_for


conn = sqlite3.connect(r'C:\Users\posinski\PycharmProjects\Dash\dash_project\backend\Sqlite-Data\example.db')




app = Flask(__name__)
data = ''

def update_data(interval):
    Timer(interval, update_data, [interval]).start()
    res1 = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/1')
    res2 = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/2')
    res3 = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/3')
    res4 = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/4')
    res5 = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/5')
    res6 = requests.get(f'http://tesla.iem.pw.edu.pl:9080/v2/monitor/6')
    json1 = res1.json()
    json2 = res2.json()
    json3 = res3.json()
    json4 = res4.json()
    json5 = res5.json()
    json6 = res6.json()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    conn = sqlite3.connect('Sqlite-Data/example.db')
    conn.execute(
        "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, 1)" % (
        dt_string, int(json1['trace']['sensors'][0]['value']), int(json1['trace']['sensors'][1]['value']),
        int(json1['trace']['sensors'][2]['value']), int(json1['trace']['sensors'][3]['value']),
        int(json1['trace']['sensors'][4]['value']), int(json1['trace']['sensors'][5]['value'])))
    conn.execute(
        "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, 2)" % (
            dt_string, int(json2['trace']['sensors'][0]['value']), int(json2['trace']['sensors'][1]['value']),
            int(json2['trace']['sensors'][2]['value']), int(json2['trace']['sensors'][3]['value']),
            int(json2['trace']['sensors'][4]['value']), int(json2['trace']['sensors'][5]['value'])))
    conn.execute(
        "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, 3)" % (
            dt_string, int(json3['trace']['sensors'][0]['value']), int(json3['trace']['sensors'][1]['value']),
            int(json3['trace']['sensors'][2]['value']), int(json3['trace']['sensors'][3]['value']),
            int(json3['trace']['sensors'][4]['value']), int(json3['trace']['sensors'][5]['value'])))
    conn.execute(
        "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, 4)" % (
            dt_string, int(json4['trace']['sensors'][0]['value']), int(json4['trace']['sensors'][1]['value']),
            int(json4['trace']['sensors'][2]['value']), int(json4['trace']['sensors'][3]['value']),
            int(json4['trace']['sensors'][4]['value']), int(json4['trace']['sensors'][5]['value'])))
    conn.execute(
        "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, 5)" % (
            dt_string, int(json5['trace']['sensors'][0]['value']), int(json5['trace']['sensors'][1]['value']),
            int(json5['trace']['sensors'][2]['value']), int(json5['trace']['sensors'][3]['value']),
            int(json5['trace']['sensors'][4]['value']), int(json5['trace']['sensors'][5]['value'])))
    conn.execute(
        "INSERT INTO data_from_tesla (date_of_measurmenet,l1,l2,l3,r1,r2,r3,person_id) VALUES ('%s', %s, %s,%s, %s, %s, %s, 6)" % (
            dt_string, int(json6['trace']['sensors'][0]['value']), int(json6['trace']['sensors'][1]['value']),
            int(json6['trace']['sensors'][2]['value']), int(json6['trace']['sensors'][3]['value']),
            int(json6['trace']['sensors'][4]['value']), int(json6['trace']['sensors'][5]['value'])))
    conn.commit()
    conn.close()

update_data(0.1)

@app.route('/')
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run()


