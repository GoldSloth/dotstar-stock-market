import Requester
import Animator
import math

numberOfPixels = 30

aapl = Requester.Requester("", "")
coloursArray = aapl.getMarketAverageColours()

try:
    strip = Animator.Animation(numberOfPixels, delay_time=1)

    strip.animateFromArray(coloursArray[0:30])

    strip.stop()

except (KeyboardInterrupt, Exception) as ex:
    print(ex)
    strip.stop()
