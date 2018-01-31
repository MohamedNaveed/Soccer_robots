import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def display_hsv(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_MOUSEMOVE:
        print cv2.cvtColor(np.uint8([[img[y,x]]]),cv2.COLOR_BGR2HSV)

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    cap.set(3,1920)
    cap.set(4,1080)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image',display_hsv)

    while(1):
        global img
        ret, frame = cap.read()

        height, width = frame.shape[:2]
        img = cv2.resize(frame,(int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_CUBIC)
        # cv2.putText(img,"Hello World!!!", (10,200), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
