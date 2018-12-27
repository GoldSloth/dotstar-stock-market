import Requester
import Animator
import math

numberOfPixels = 30

aapl = Requester.Requester("", "")

# aapl.getData()

try:
    strip = Animator.Animation(numberOfPixels)
    testArr = []
    for i in range(numberOfPixels):
        testArr.append([math.sin(i/1000), math.cos(i/1000), 1 - math.sin(i/1000)])
    strip.animateFromArray(testArr)

except (KeyboardInterrupt, Exception) as ex:
    print(ex)
    strip.stop()
