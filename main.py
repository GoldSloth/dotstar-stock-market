import Requester
import Animator
import math

numberOfPixels = 30

aapl = Requester.Requester("aapl", "20181228")
coloursArray = aapl.getMarketAverageColours()

try:
    strip = Animator.Animation(numberOfPixels, delay_time=0.5)

    strip.animateFromArray(coloursArray[0:30])

    strip.stop()

except (KeyboardInterrupt, Exception) as ex:
    print(ex)
    strip.stop()
