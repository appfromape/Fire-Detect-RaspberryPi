#!/usr/bin/python3
# coding: UTF-8

from flask import Flask, render_template
from flask import request, jsonify
import requests
import json
import os #為了使用系統 terminal
import netifaces as ni

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[2][0]['addr']

def get(url):
    try:
        res = requests.get(url)
        return res.json()
    except:
        return False

app = Flask(__name__)

@app.route('/')

def index():

    data = get('<ip address>:3000/alocovalue') # get data from google cloud plateform for alcohol sensor.

    img1 = './static/redcup.png'
    img2 = './static/greencup.png'
    img3 = './static/yellowcup.png'
    img4 = './static/graycup.png'
    
    if data[u'level'] == "1":
        return render_template('index1.html', img1 = img2 , img2 = img4 ,img3 = img4)
    elif data[u'level'] == "2":
        return render_template('index1.html', img1 = img4 , img2 = img3 ,img3 = img4)   
    else:
        return render_template('index1.html', img1 = img4 , img2 = img4 ,img3 = img1)
    

if __name__ == "__main__":
    app.run(debug=True, host=ip, port=8002)
