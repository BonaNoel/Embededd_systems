from time import sleep
from sense_hat import SenseHat
import random

sense = SenseHat()

# Generate a random color


def random_colour():
    # randint - random integer between an interval
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    return (random_red, random_green, random_blue)


sense.show_letter("N", random_colour())
# sleep - temporarily pause your program
sleep(1)
sense.show_letter("O", random_colour())
sleep(1)
sense.show_letter("E", random_colour())
sleep(1)
sense.show_letter("L", random_colour())
sleep(1)

sense.clear()
