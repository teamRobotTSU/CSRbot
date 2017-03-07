import RPi.GPIO as GPIO
from time import sleep

Motor1E = 15
Motor1A = 35
Motor1B = 37

Motor2E = 18
Motor2A = 16
Motor2B = 12


class Move:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Motor1E, GPIO.OUT)
        GPIO.setup(Motor1A, GPIO.OUT)
        GPIO.setup(Motor1B, GPIO.OUT)
        self.p1 = GPIO.PWM(Motor1E, 100)

        GPIO.setup(Motor2E, GPIO.OUT)
        GPIO.setup(Motor2A, GPIO.OUT)
        GPIO.setup(Motor2B, GPIO.OUT)
        self.p2 = GPIO.PWM(Motor2E, 100)
        
        self.vel = 0 #Used to maintain speed if no change of direction
        print("success.")
        
        
    #************* STOP ***************
    def stop(self, speed):
        mina = int(speed/4)
        maxa = int(speed) 
        step = int(mina)
        #Ramp down then stop
        for x in range(maxa, mina-step, -step):
            self.p1.start(x)
            self.p2.start(x)
            print(x)
            sleep(.25) 
        self.p1.stop()
        self.p2.stop()
        self.vel = 0
        return

        
    #************* FORWARD ***************
    def forward(self, speed):
        mina = int(speed/4)
        maxa = int(speed) 
        step = int(mina)
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B, GPIO.LOW)
        if self.vel is 0:
            for x in range(mina, (maxa+25), step):
                self.p1.start(x)
                self.p2.start(x)
                print(x)
                sleep(.25)
            self.vel = 100
        self.p1.start(speed)
        self.p2.start(speed)
        return
       

    #*********** BACKWARDS **************
    def backward(self, speed):
        mina = int(speed/4)
        maxa = int(speed) 
        step = int(mina)
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor2A, GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        if self.vel is 0:
            for x in range(mina, (maxa+25), step):
                self.p1.start(x)
                self.p2.start(x)
                print(x)
                sleep(.25)
            self.vel = 100
        self.p1.start(speed)
        self.p2.start(speed)
        return
       

    #************* TURN ***************
    def turn(self, leftWheelSpeed, rightWheelSpeed):
        mina = int(speed/4)
        maxa = int(speed) 
        step = int(mina)
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B, GPIO.LOW)
        if self.vel is 0:
            for x in range(mina, (maxa+25), step):
                self.p1.start(x)
                self.p2.start(x)
                print(x)
                sleep(.25)
            self.vel = 100
        self.p1.start(leftWheelSpeed)
        self.p2.start(rightWheelSpeed)
        return

    









