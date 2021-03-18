#!/usr/bin/python3
# coding: UTF-8

from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
import os #為了使用系統 terminal
import netifaces as ni

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[2][0]['addr']

GPIO_INPUT = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_INPUT, GPIO.IN)

app = Flask(__name__)

@app.route('/')
def index():
	title = 'Fire Detector System'
	img = './static/fire.png'
	img2 = './static/fireblue.png'

	if GPIO.input(GPIO_INPUT) == GPIO.LOW:
		return render_template('index.html', title=title, img=img)
	else:
		return render_template('index.html', title=title, img=img2)

if __name__ == "__main__":
	app.run(debug=True, host=ip, port=7002)
