import Requester
import Animator
import math

numberOfPixels = 30

aapl = Requester.Requester("20181226", "aapl")
coloursArray = aapl.getMarketAverageColours()

try:
    strip = Animator.Animation(numberOfPixels, delay_time=0.08)

    strip.animateFromArray(coloursArray)

    strip.stop()

except (KeyboardInterrupt, Exception) as ex:
    print(ex)
    strip.stop()
