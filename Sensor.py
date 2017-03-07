import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)



class Sensors:
  def __init__(self, LIREC = 0,RIREC = 0, LIRLED = 0,RIRLED = 0, ECHO = 0, TRIG = 0,ledA = 0, ledB = 0, pir = 0,PhotoPin = 0):
    print("Object Created")
    self.ECHO = 18
    self.TRIG = 22
    GPIO.setup(self.TRIG,GPIO.OUT)
    GPIO.setup(self.ECHO,GPIO.IN)
    GPIO.output(self.TRIG, False)

    self.ledA = 7
    self.ledB = 15
    GPIO.setup(self.ledA, GPIO.OUT)
    GPIO.setup(self.ledB, GPIO.OUT)

    self.pir = 36
    GPIO.setup(self.pir, GPIO.IN)

    self.PhotoPin = 11
    GPIO.setup(self.PhotoPin, GPIO.OUT)

    self.RIRLED = 38
    self.LIRLED = 40
    GPIO.setup(self.RIRLED,GPIO.OUT)
    GPIO.setup(self.LIRLED,GPIO.OUT)

    self.LIREC = 12
    self.RIREC = 35
    GPIO.setup(self.LIREC, GPIO.IN)
    GPIO.setup(self.RIREC, GPIO.IN)

    

  def SonicRange(self):
    print ("Distance Measurement In Progress")
    print ("Allow Module to Settle")
    time.sleep(0.5)
    print ("Settled")
    GPIO.output(self.TRIG, True)
    time.sleep(0.00001)
    GPIO.output(self.TRIG,False)
    pulse_start = time.time()
    while GPIO.input(self.ECHO)==0:
      pulse_start = time.time()
    while GPIO.input(self.ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end-pulse_start
    distance = pulse_duration*17150
    return distance
  def LED(self):
    i = 0
    GPIO.output(self.ledA, 1)
    GPIO.output(self.ledB,1)
    time.sleep(1)
    GPIO.output(self.ledA,0)
    GPIO.output(self.ledB,0)
  def PIR(self):
    status = True
    while status:
      i = GPIO.input(self.pir)
      if i == 0:
        print (" No intruders")
      elif i == 1:
        print ("Intruders")
        self.LED()
        status = False
  def PhotoRes(self):
    count = 0
    GPIO.output(self.PhotoPin,GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(self.PhotoPin,GPIO.IN)
    while (GPIO.input(self.PhotoPin) == GPIO.LOW):
      count+=1
    return count

  def IRTrans(self):
    
    GPIO.output(self.LIRLED, 1)
    GPIO.output(self.RIRLED,1)
    self.IRRec()
    GPIO.output(self.LIRLED,0)
    GPIO.output(self.RIRLED,0)
    
  def IRRec(self):
    stat = True
    newcount = 0
    while stat:
      newcount+=1
      LeftInput = GPIO.input(self.LIREC)
      RightInput = GPIO.input(self.RIREC)
      if LeftInput == 1 and RightInput == 1:
        print ("Surface there")
      elif LeftInput == 0 or RightInput == 0:
        print ("No Surface | RightInput =", RightInput, "Left Input =", LeftInput, "count", newcount)
        ##self.LED()
        stat = False

def destroy():
  GPIO.cleanup()
    
def main():
  a = Sensors()
  try:
    print("Distance from object", a.SonicRange(), "cm")
    a.LED()
    a.PIR()
    print("Time to charge Capacitor", a.PhotoRes(), "loops")
    a.IRTrans()
    ##a.IRRec()
  except KeyboardInterrupt:
    destroy()
  finally:
    destroy()
  
if __name__ == '__main__':
  main()
