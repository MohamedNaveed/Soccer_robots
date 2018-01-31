import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

cap = cv2.VideoCapture(1)
cap.set(3,1920)
cap.set(4,1080)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    height, width = frame.shape[:2]
    res = cv2.resize(frame,(int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_CUBIC)

    hsv = cv2.cvtColor(res,cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    # plt.imshow(hsv, cmap = 'gray', interpolation = 'bicubic')
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()
    cv2.imshow("HSV",hsv)
    cv2.imshow("RGB",res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
