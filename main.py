import Requester
import Animator
import math

aapl = Requester.Requester("", "")

# aapl.getData()

try:
    strip = Animator.Animation(30)
    testArr = []
    for i in range(30):
        testArr.append([math.sin(i), math.cos(i), 1 - math.sin(i)])
    strip.animateFromArray(testArr)

except (KeyboardInterrupt, Exception) as ex:
    print(ex)
    strip.stop()