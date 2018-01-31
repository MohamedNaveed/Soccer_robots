import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3,1920)
cap.set(4,1080)

flag = 0
while(True):
    ret, image = cap.read()
    height, width = image.shape[:2]
    image = cv2.resize(image,(int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_CUBIC)
    boundaries = [([60,110,40],[130,170,125])]
    for (lower, upper) in boundaries:
    	# create NumPy arrays from the boundaries
    	lower = np.array(lower, dtype = "uint8")
    	upper = np.array(upper, dtype = "uint8")

    	# find the colors within the specified boundaries and apply
    	# the mask
    	mask = cv2.inRange(image, lower, upper)
    	output = cv2.bitwise_and(image, image, mask = mask)

    	# show the images
    	cv2.imshow("images", np.hstack([image, output]))
    	if cv2.waitKey(1) & 0xFF == ord('q'):
            flag = 1
            break
    if flag == 1:
        break
        cv2.destroyAllWindows()
