import cv2
import numpy as np
import cv2
import numpy as np
import keras
from keras import backend as K
from keras.optimizers import Adam
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt
 
cam = cv2.VideoCapture(0)
 
mobile = keras.applications.mobilenet.MobileNet()
 
def prepare_image(img):
	img_resized = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
	img_array_expanded_dims = np.expand_dims(img_resized, axis=0)
	return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('my_cam_vis.avi', fourcc, 20.0, (640, 480))
while True:
	ret, img = cam.read()
	preprocessed_image = prepare_image(img)
	predictions = mobile.predict(preprocessed_image)
	results = imagenet_utils.decode_predictions(predictions)
 
	print(results)
	cv2.imshow('my_cam', img)	
	if cv2.waitKey(10) == 27:
			break
cam.release()
out.release()
cv2.destroyAllWindows() 
