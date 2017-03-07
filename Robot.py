import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

from Behavior import Behave
from Move import Move
from Sense import Sense
from Vision import Vision
from Communicate import Communicate

class Robot(object): #147
    def __init__(self):
        self.move = Move()
        self.behave = Behave()
        self.sense = Sense()
        self.vision = Vision()
        self.stopThread = False
        self.communicate = Communicate("")
        self.retrieveMessagesThread = Thread(target=self.retrieveMessages)
        self.retrieveMessagesThread.start()
        
    def retrieveMessages(self):
        while not self.stopThread:
            while len(self.communicate.inbox) > 0:
                msg = self.communicate.inbox.pop()
                print(msg)
                if(msg == "hey"):
                    print("yes it equals hey.")
                    self.communicate.sendMessage("got it!!!!!!")

robot = Robot()
#robot.communicate.setupLine("192.168.1.147") #connects to a server
robot.communicate.setupLine("") #is a server


count = 0
try:
    while(True):
        print("in main doing stuff.")
        sleep(1)
        count += 1
        #if count == 3:
        #    robot.communicate.sendMessage("hey")


except KeyboardInterrupt:
    print("exiting.")
    robot.stopThread = True
    robot.communicate.closeConnection()
    robot.checkMessagesThread.join()
    GPIO.cleanup()


