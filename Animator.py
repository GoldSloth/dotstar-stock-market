import time
from dotstar import Adafruit_DotStar

def Color(red, green, blue, white=0):
    return int((white * pow(2, 24)) + (red * pow(2, 16)) + (green * pow(2, 8)) + blue)

class Animation:
    def __init__(self, numpixels, delay_time=0.02, brightness=16):
        self.numpixels = numpixels
        self.delay_time = delay_time

        self.strip = Adafruit_DotStar(numpixels, 12000000)
        self.strip.begin()

        self.strip.setBrightness(brightness)
    
    def animateFromArray(self, data):
        self.data = data
        for pixelNum in range(len(self.data)):
            pixelColor = Color(self.data[pixelNum][0] * 255, self.data[pixelNum][1] * 255, self.data[pixelNum][2] * 255)
            self.strip.setPixelColor(pixelNum, pixelColor)
            self.strip.show()
            time.sleep(self.delay_time)
    
    def stop(self):
        self.strip.clear()
        self.strip.show()
        self.strip.close()