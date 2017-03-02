import time
from time import sleep
import RPi.GPIO as GPIO
from Behavior import Behave
from threading import Thread
import multiprocessing

def moveServo(cmd):
    name = multiprocessing.current_process().name
    print(str(cmd) + " " + str(name))
    return


def action():
    p = multiprocessing.Process(target=moveServo, args=("move 1",))
    p.start()
    time.sleep(.2)
    p = multiprocessing.Process(target=moveServo, args=("move 2",))
    p.start()
    time.sleep(.2)
    p = multiprocessing.Process(target=moveServo, args=("move 3",))
    p.start()
    time.sleep(.2)
    return

#action()


behave = Behave()

#behave.tryAgain()
behave.hint()
#behave.lowBattery()
#behave.success()
#behave.happy()
#noThread = Thread(target=behave.tryAgain)
#noThread.start()
#noThread.join()

#waitingThread = Thread(target=behave.waiting)
#waitingThread.start()
#waitingThread.join()

#waitingThread = Thread(target=behave.waiting)
#waitingThread.start()
#waitingThread.join()

#successThread = Thread(target=behave.success)
#successThread.start()
#successThread.join()




GPIO.cleanup()

