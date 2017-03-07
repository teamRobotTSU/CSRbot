import RPi.GPIO as GPIO
import smbus
import os
import sys
import termios
import tty

bus = smbus.SMBus(1)
gyroAddress = 0x68

Motor1E = 15
Motor1A = 35
Motor1B = 37

Motor2E = 18
Motor2A = 16
Motor2B = 12

buzzer = 29
greenLED = 36
green1LED = 32
yellowLED = 38
redLED = 40
panServo = 12
tiltServo = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor2E, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
pwm1 = GPIO.PWM(Motor1E, 100)
pwm2 = GPIO.PWM(Motor2E, 100)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(green1LED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(panServo, GPIO.OUT)
GPIO.setup(tiltServo, GPIO.OUT)

def getKey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    k = None
    try:
        k = os.read(fd, 3)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    key = str(k)
    key = key.replace("b", "")
    key = key.replace("'", "")
    return key

def hardwareCleanup():
    GPIO.cleanup()
    return

def tilt(direction):
    if direction == "u":
        os.system("echo 1=+1 > /dev/servoblaster")
    elif direction == "c":
        os.system("echo 1=150 > /dev/servoblaster")
    elif direction == "d":
        os.system("echo 1=-1 > /dev/servoblaster")
    return

def pan(direction):
    if direction == "l":
        os.system("echo 2=+1 > /dev/servoblaster")
    elif direction == "c":
        os.system("echo 2=150 > /dev/servoblaster")
    elif direction == "r":
        os.system("echo 2=-1 > /dev/servoblaster")
    return

os.system("sudo /home/pi/csrbot1/PiBits/ServoBlaster/user/servod")
os.system("echo 1=150 > /dev/servoblaster")
os.system("echo 2=150 > /dev/servoblaster")




    




