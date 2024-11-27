import cv2
import numpy as np
 
cam = cv2.VideoCapture(0)
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('my_cam_vis.avi', fourcc, 20.0, (640, 480))
while True:
	ret, img = cam.read()
	cv2.imshow('my_cam', img)	
	if cv2.waitKey(10) == 27:
			break
cam.release()
out.release()
cv2.destroyAllWindows()
 
