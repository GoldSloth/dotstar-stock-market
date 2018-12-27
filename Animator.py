import time
from dotstar import Adafruit_DotStar

class Animation:
    def __init__(self, numpixels, delay_time=0.02, brightness=16):
        self.numpixels = numpixels
        self.delay_time = delay_time

        self.strip = Adafruit_DotStar(numpixels, 12000000)
        self.strip.begin()

        self.strip.setBrightness(brightness)
    
    def animateFromArray(self, data):
        for pixelNum in range(len(data)):
            print([255, data[pixelNum] * 255, data[pixelNum] * 255])
            self.strip.setPixelColor(pixelNum, 255, int(data[pixelNum] * 255), int(data[pixelNum] * 255))
            self.strip.show()
            time.sleep(self.delay_time)
    
    def stop(self):
        self.strip.clear()
        self.strip.show()
        self.strip.close()