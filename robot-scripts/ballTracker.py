from robot-api/VideoStream import VideoStream
from robot-api/Robot import Move, Behave
import datetime
import numpy as np
import RPi.GPIO as GPIO
from collections import deque
import argparse
import imutils
import time
import cv2
from threading import Thread

Move.__init__(Move)
Behave.__init__(Behave)
Move.stop()
#Behave.test()
#Behave.no()
#Behave.success()

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--picamera", type=int, default=1, help="use piCam? 1 for yes, 0 for no")
parser.add_argument("-b", "--buffer", type=int, default=64, help="max track points: default 64")
args = vars(parser.parse_args())

stream = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(.5)


#HSV color space
lowOrange = (4, 192, 192)
highOrange = (16, 255, 255)

lowYellow = (20, 100, 100)
highYellow = (40, 255, 255)

lowGreen = (36, 160, 64)
highGreen = (75, 210, 192)

lowBlue = (98, 128, 64)
highBlue = (132, 255, 200)

lowRed1 = (170,50,50)
highRed1 = (179, 255, 255)
lowRed0 = (0, 50, 50)
highRed0 = (10, 255, 255)

trackPoints = deque(maxlen=args["buffer"])
areas = deque(maxlen=3)
avgArea = 0
pointCounter = 0
area = 0
(dX, dY) = (0,0)
direction = ""
drawLine = False
trackCounter = 0
imNum = 0
tCount = 0
threshold = 0
found = False
getThreshold = 0

def driveRobot(area):
    if area < (threshold - .20*threshold):
        Move.forward(255, .02)
    elif area > (threshold + .20*threshold):
        Move.backward(255, .02)
    #Move.stop()
    return

def moveRobot(xPos, xSpd):
    if xPos > 25:
        if xSpd > 0 and xSpd < 50:
            Move.rightTurn(255, 255, .01)
        elif xSpd >=50 and xSpd < 100:
            Move.rightTurn(255, 255, .03)
        elif xSpd >= 100 and xSpd < 200:
            Move.rightTurn(255, 255, .05)
        elif xSpd >= 200 and xSpd < 300:
            Move.rightTurn(255, 255, .08)
        elif xSpd >= 300:
            Move.rightTurn(255, 255, .11)
        else:
            Move.rightTurn(255, 255, .01)
        Move.stop()
    if xPos < -25:
        if xSpd < 0 and dX > -50:
            Move.leftTurn(255, 255, .01)
        elif xSpd <=-50 and xSpd > -100:
            Move.leftTurn(255, 255, .02)
        elif xSpd <= -100 and xSpd > -200:
            Move.leftTurn(255, 255, .05)
        elif xSpd <= -200 and xSpd > -300:
            Move.leftTurn(255, 255, .08)
        elif xSpd <= -300:
            Move.leftTurn(255, 255, .11)
        else:
            Move.leftTurn(255, 255, .01)  
        Move.stop()
    return
    
def processFrame(frame):
    if not found:
        cv2.circle(frame, (cX,cY), 50, (0,255,255), 1)
    else:
        cv2.circle(frame, (cX,cY), 50, (255,0,255), 2)
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #maskedFrame = cv2.inRange(hsvFrame, lowYellow, highYellow)
    #maskedFrame = cv2.inRange(hsvFrame, lowGreen, highGreen)
    #maskedFrame = cv2.inRange(hsvFrame, lowOrange, highOrange)
    maskedFrame = cv2.inRange(hsvFrame, lowBlue, highBlue)
    #maskedFrame0 = cv2.inRange(hsvFrame, lowRed0, highRed0)
    #maskedFrame1 = cv2.inRange(hsvFrame, lowRed1, highRed1)
    #maskedFrame = maskedFrame0+maskedFrame1
    maskedFrame = cv2.erode(maskedFrame, None, iterations=2)
    maskedFrame = cv2.dilate(maskedFrame, None, iterations=2)

    return maskedFrame

#falseCount = 0
noCount = 0
noThread = Thread(target=Behave.no)
sucThread = Thread(target=Behave.success)
try:
    while(True):
        if not getThreshold == 2:
            if noCount > 40:
                noThread = Thread(target=Behave.no)
                noThread.start()
                #Behave.no()
                noCount = 0
            else:
                noCount += 1
        frame = stream.read()
        frame = imutils.resize(frame, width=600, height=400)
        (cX, cY) = (frame.shape[1] // 2, frame.shape[0] // 2)
        ((x, y), radius) = ((cX, cY), 15)
        
        processedFrame = processFrame(frame)

        contours = cv2.findContours(processedFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = (330,225)
        
        if(len(contours) > 0):
            contour = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            moment = cv2.moments(contour)
            center = (int(moment["m10"]/moment["m00"]), int(moment["m01"]/moment["m00"]))
            #print(radius)

            if(radius > 10):
                area = 3.1415 * (radius * radius)
                areas.appendleft(area)
                if len(areas) == 3:
                    avgArea = 0
                    for a in areas:
                        avgArea = avgArea + int(a)
                    avgArea = avgArea / 3
                    if tCount < 5 and getThreshold == 1:
                        threshold = threshold + avgArea
                        tCount += 1
                    if tCount == 5:
                        threshold = threshold / 6
                        threshold = int(threshold)
                        tCount += 1
                        getThreshold = 2
                        while noThread.isAlive():
                            print("")
                        sucThread.start()
                        #print("target acquired.")
                        
                    areas.clear()
                    
               # cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 4, (0, 0, 255), -1)
                trackPoints.appendleft(center)
                drawLine = True
        else:
            trackCounter += 1
            center = (0,0)
            if(trackCounter == 20):
                drawLine = False
                trackPoints.clear()
                trackCounter = 0
                continue
                
        for i in range(1, len(trackPoints)):
            if(trackPoints[i-1] is None or trackPoints[i] is None):
                continue
            if(pointCounter >= 10 and i == 10 and trackPoints[i-10] is not None):
                dX = trackPoints[i-10][0] - trackPoints[i][0]
                dY = trackPoints[i-10][1] - trackPoints[i][1]
           
        cv2.imshow("Frame", frame)
        pointCounter += 1
        found = False
        if(len(trackPoints) > 5):
            inRange = False
            if tCount == 6 or getThreshold == 0:
                if getThreshold == 2:
                    if (x-cX) > 30 or (x-cX) < -30: 
                        mThread = Thread(target=moveRobot, args=((x-cX), dX))
                        mThread.start()
                        mThread.join()
                    if avgArea > (threshold + .3*threshold) or avgArea < (threshold - .3*threshold):
                        #print(threshold)
                        #print(avgArea)
                        mThread = Thread(target=driveRobot, args=(avgArea,))
                        mThread.start()
                        mThread.join()
                        time.sleep(.05)
                        inRange = False
                        #falseCount += 1
                        #print(falseCount)
                    else:
                        inRange = True
                        falseCount = 0
                        Move.stop()
                    if found and inRange:
                        time.sleep(5)
                if center[0] < 350 and center[0] > 250:
                    if center[1] < 275 and center[1] > 175:
                        #print(center)
                        found = True
                        if getThreshold == 0:
                            getThreshold = 1
                        if inRange:
                            if imNum % 25 == 0:
                                cv2.imwrite("capture%i.jpg" %(imNum / 25), frame)
                            imNum += 1
        #if noThread.isAlive():
            #noThread.join()
        #cv2.imshow("masked frame", maskedFrame)
        if(cv2.waitKey(1) & 0xFF == ord("q")):
            break
except KeyboardInterrupt:
    print("ending routine....")
finally:
    cv2.destroyAllWindows()
    stream.stop()
    GPIO.cleanup()
    
    
