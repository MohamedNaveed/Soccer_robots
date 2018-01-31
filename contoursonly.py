#import cv
import cv2
import numpy as np
import math
#import socket

#TCP_IP = '192.168.43.130'
#TCP_PORT = 8080
#BUFFER_SIZE = 1024

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
#s.listen(1)

#conn, addr = s.accept()
#print 'Connection address:', addr

WIDTH  = 1100
HEIGHT = 620

cap = cv2.VideoCapture(1)
cap.set(3,1920) #3 - WIDTH
cap.set(4,1080)  #4 - HEIGHT
#img = cv2.imread('',0)
#cv2.imshow("Image",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cX = 0; cY = 0; yawAngle = 0; yY = 0; yX = 0;
while(True):
    flag = 0
    ret, image = cap.read()

    # height, width = image.shape[:2]
    # res = cv2.resize(image,(int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_CUBIC)

    # cv2.imshow("Original_resized",res)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    flag = 1
    #    break

    pts1 = np.float32([[195,5],[1775,12],[1791,925],[220,991]])
    pts2 = np.float32([[0,0],[WIDTH,0],[WIDTH,HEIGHT],[0,HEIGHT]])

    M = cv2.getPerspectiveTransform(pts1,pts2)
    img = cv2.warpPerspective(image,M,(WIDTH,HEIGHT))

    cv2.imshow("Perspective",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       flag = 1
       break

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(imgGray,250,255,cv2.THRESH_BINARY)

    cv2.imshow("Thresh",thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        flag = 1
        break

    _,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, 2)

    positions = list()
    j = 0
    for i in range(len(contours)):
        c = contours[i]
        area = cv2.contourArea(c)
        if(area > 500 and area < 5000):
            j += 1
            # print "Area" , area
            M = cv2.moments(c)
            if M["m00"] == 0:
                continue
            cv2.drawContours(img, [c], -1, (0, 255, 0), 2)

            cnt = contours[hierarchy[0][i][2]]
            areaSmall = cv2.contourArea(cnt)
            # print "Area small", areaSmall
            Msmall = cv2.moments(cnt)
            if Msmall["m00"] == 0:
                continue
            yX = int(Msmall["m10"] / Msmall["m00"])
            yY = int(Msmall["m01"] / Msmall["m00"])
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)

            cv2.imshow("Image",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                flag = 1
                break

            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            yawAngle = math.atan2(cY-yY,cX-yX)*180/math.pi

            position = dict()
            position.update({"bot":j,"cX":cX, "cY":cY, "theta":yawAngle})

            positions.append(position)

    # print "Number of contours: ",j
    if flag == 1:
        break

    for position in positions:
        string = "Bot number: " + str(position["bot"]) + " "
        string += "cX: " + str(position["cX"]) + " cY: " + str(position["cY"]) + " Yaw: " + str(position["theta"])
        print string
        print '\n'
    #data = conn.recv(BUFFER_SIZE)
    #if not data: continue
    #conn.send(string)
#conn.close()
cap.release()
cv2.destroyAllWindows()
