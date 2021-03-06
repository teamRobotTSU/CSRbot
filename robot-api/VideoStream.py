from threading import Thread
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
#import time
import datetime
import uuid
import os

#This class is used to approximate the processing frames per second
#This class has no functional purpose per se, strictly for information
class FPS:
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        self._end = datetime.datetime.now()

    def update(self):
        self._numFrames += 1

    def elapsed(self):
        return(self._end - self._start).total_seconds()

    def fps(self):
        return self._numFrames / self.elapsed()

#This class threads the camera read
class WebcamVideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while(True):
            if(self.stopped):
                return
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = true

class PiVideoStream:
    def __init__(self, resolution=(320, 240), framerate=32):
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)

        self.frame = None
        self.stopped = False

    def start(self):
        #self.update()
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        for f in self.stream:
            self.frame = f.array
            self.rawCapture.truncate(0)

            if(self.stopped):
               self.stream.close()
               self.rawCapture.close()
               self.camera.close()
               return

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True


class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240), framerate=32):
        if usePiCamera:
            self.stream = PiVideoStream(resolution=resolution, framerate=framerate)
        else:
            self.stream = WebcamVideoStream(src=src)
        
    def start(self):
        return self.stream.start()

    def update(self):
        self.stream.update()

    def read(self):
        return self.stream.read()

    def stop(self):
        self.stream.stop()

class TempImage:
	def __init__(self, basePath="./", ext=".jpg"):
		# construct the file path
		self.path = "{base_path}/{rand}{ext}".format(base_path=basePath,
			rand=str(uuid.uuid4()), ext=ext)
 
	def cleanup(self):
		# remove the file
		os.remove(self.path)









    
