#!/usr/bin/python3
# coding: UTF-8

import RPi.GPIO as GPIO #為了讀取針腳
import requests #為了使用 line notify
import os #為了使用系統 terminal
import picamera #為了使用相機
import time #為了使用時間 delay
import netifaces as ni

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[2][0]['addr']

def iplocation():
	payload = {'message':ip}
	headers = {'Authorization': 'Bearer ' + 'your line notify toden'}
	requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)

os.system("sudo service motion start")
os.system("lxterminal -e python3 ./app.py")
os.system("lxterminal -e python3 ./app1.py")
iplocation()
time.sleep(1)

def takepic():
	os.system("sudo service motion stop")
	time.sleep(1)
	camera = picamera.PiCamera()
	time.sleep(1) # Camera warm-up time
	camera.capture('danger.jpg')
	camera.close()

def makenoice():
	GPIO.setwarnings(False)
	GPIO.setup(12, GPIO.OUT)
	p = GPIO.PWM(12, 50)
	p.start(50)
	p.ChangeFrequency(650)
	time.sleep(0.4)
	p.ChangeFrequency(750)
	time.sleep(0.6)
	p.ChangeFrequency(650)
	time.sleep(0.4)
	p.ChangeFrequency(750)
	time.sleep(0.6)
	p.ChangeFrequency(650)
	time.sleep(0.4)
	p.ChangeFrequency(750)
	time.sleep(0.6)

def line_notify():
	picURI = "/home/pi/Desktop/flask/danger.jpg"
	payload = {'message':'失火警報!!!!!'}
	headers = {'Authorization': 'Bearer ' + 'your line notify toden'}
	files = {'imageFile': open(picURI, 'rb')}
	requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers, files = files)

try:
	while True:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(14, GPIO.IN)
	
		if GPIO.input(14) == GPIO.LOW:
			takepic()
			line_notify()
			makenoice()
			print("smoke detected")
			time.sleep(1)
			
		else:
			os.system("sudo service motion start")
			print("runninng")
			time.sleep(1)
	
except KeyboardInterrupt:
	print("stopped")
	GPIO.cleanup()
