import cv2
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
 
LED_PIN=2
 
Servo_pin=3
 
button_pin = 4
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(Servo_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
pwm = GPIO.PWM(Servo_pin, 50)
pwm.start(0)
 
def change_diod_signal(sig):
	GPIO.output(LED_PIN, sig)
	print(f'face found = {sig}')
 
def change_angle(angle):
	duty=angle/18+2
	GPIO.output(Servo_pin, True)	
	pwm.ChangeDutyCycle(duty)
 
 
 
cam = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('my_cam_vis.avi', fourcc, 20.0, (640, 480))
angle = 180
while True:
	print(f'button pressed ? {GPIO.input(button_pin)}')
 
	face_found = False
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	faces_rect = classifier.detectMultiScale(
		gray, scaleFactor=1.1, minNeighbors=9)
 
	if(len(faces_rect)>0):
		face_found=True
	else:
		face_found=False
	change_diod_signal(face_found)
 
	for (x, y, w, h) in faces_rect:
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
		cv2.rectangle(img, (x+w//2-1, y), (x + w//2+1, y + h), (255, 0, 0), thickness=2)
		cv2.rectangle(img, (319, 480), (320, 480), (0, 0, 255), thickness=2)
		cv2.rectangle(img, (319, 239), (x+w//2-1, 240), (150, 0, 0), thickness=2)
		if (x+w//2-1 > 319):
			print('turn left')
			if angle < 359:
				angle = + 1
			else:
				angle = 0		
		else:
			print('turn right')
			if angle > 0:
				angle = - 1
			else:
				angle = 359
		face_found = True
	change_angle(angle)
	cv2.imshow('my_cam', img)	 
	if cv2.waitKey(10) == 27:
			break
cam.release()
out.release()
cv2.destroyAllWindows()
