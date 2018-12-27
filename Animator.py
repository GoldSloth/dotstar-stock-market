import time
from dotstar import Adafruit_DotStar

def Colour(red, green, blue, white=0):
    return int((white * pow(2, 24)) + (blue * pow(2, 16)) + (green * pow(2, 8)) + red)

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
            pixelColor = Colour(255, data[pixelNum] * 255, data[pixelNum] * 255)
            self.strip.setPixelColor(pixelNum, pixelColor)
            self.strip.show()
            time.sleep(self.delay_time)
    
    def stop(self):
        self.strip.clear()
        self.strip.show()
        self.strip.close()