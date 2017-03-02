import RPi.GPIO as GPIO
from time import sleep

Motor1E = 15
Motor1A = 35
Motor1B = 37

Motor2E = 18
Motor2A = 16
Motor2B = 12

rLED = 40
gLED = 38
buzzer = 36

class Behave:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(rLED, GPIO.OUT)
        GPIO.setup(gLED, GPIO.OUT)
        GPIO.setup(buzzer, GPIO.OUT)

    def success():
        GPIO.output(gLED, GPIO.HIGH)
        Behave.buzz(400)
        sleep(.01)
        Behave.buzz(800)
        sleep(.01)
        Behave.buzz(1400)
        GPIO.output(gLED, GPIO.LOW)
        return

    def no():
        GPIO.output(rLED, GPIO.HIGH)
        Behave.buzz(400)
        sleep(.07)
        GPIO.output(rLED, GPIO.LOW)
        sleep(.07)
        GPIO.output(rLED, GPIO.HIGH)
        Behave.buzz(200)
        sleep(.07)
        GPIO.output(rLED, GPIO.LOW)
        sleep(.07)
        return

    def yes():
        GPIO.output(rLED, GPIO.HIGH)
        Behave.buzz(400)
        sleep(.07)
        GPIO.output(rLED, GPIO.LOW)
        sleep(.07)
        GPIO.output(rLED, GPIO.HIGH)
        Behave.buzz(200)
        sleep(.07)
        GPIO.output(rLED, GPIO.LOW)
        sleep(.07)
        return
    
    def test():
        GPIO.output(rLED, GPIO.HIGH)
        sleep(.25)
        GPIO.output(rLED, GPIO.LOW)
        sleep(1)
        GPIO.output(gLED, GPIO.HIGH)
        sleep(.25)
        GPIO.output(gLED, GPIO.LOW)
        for i in range(0,5):
            Behave.buzz(200)
            sleep(.15)
        return

    def buzz(tone):
        period = 1.0 / int(tone)
        delay = period / 2
        cycles = int(.25 * int(tone))
        for i in range(cycles):
            GPIO.output(buzzer, True)
            sleep(delay)
            GPIO.output(buzzer, False)
            sleep(delay)
        return

class Move:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Motor1E, GPIO.OUT)
        GPIO.setup(Motor1A, GPIO.OUT)
        GPIO.setup(Motor1B, GPIO.OUT)

        GPIO.setup(Motor2E, GPIO.OUT)
        GPIO.setup(Motor2A, GPIO.OUT)
        GPIO.setup(Motor2B, GPIO.OUT)
        
    #************* STOP ***************
    def stop():
        GPIO.output(Motor1E, GPIO.LOW)
        GPIO.output(Motor2E, GPIO.LOW)
        
    #************* FORWARD ***************
    def forward(speed, duration):
        GPIO.output(Motor1E, GPIO.HIGH)
        GPIO.output(Motor2E, GPIO.HIGH)
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B, GPIO.LOW)
        sleep(duration)

    #*********** BACKWARDS **************
    def backward(speed, duration):
        GPIO.output(Motor1E, GPIO.HIGH)
        GPIO.output(Motor2E, GPIO.HIGH)
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor2A, GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        sleep(duration)

        #************* LEFT TURN ***************
    def leftTurn(leftSpeed, rightSpeed, duration):
        GPIO.output(Motor1E, GPIO.HIGH)
        GPIO.output(Motor2E, GPIO.HIGH)
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B, GPIO.HIGH)
        sleep(duration)

    #*********** RIGHT TURN **************
    def rightTurn(leftSpeed, rightSpeed, duration):
        GPIO.output(Motor1E, GPIO.HIGH)
        GPIO.output(Motor2E, GPIO.HIGH)
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B, GPIO.LOW)
        sleep(duration)












