from sense_hat import SenseHat
from time import sleep
import math

sense = SenseHat()

b = (0, 0, 0)
# white
w = (255, 255, 255)
# white
cat1_pixels = [
    w, w, w, w, w, w, w, w,
    b, w, w, w, w, w, w, w,
    w, b, w, w, b, w, b, w,
    w, b, b, b, b, b, b, w,
    w, b, b, b, b, w, b, b,
    w, b, b, b, b, b, b, w,
    w, b, w, b, w, b, w, w,
    w, w, w, w, w, w, w, w]

cat2_pixels = [
    w, w, w, w, w, w, w, w,
    b, w, w, w, w, w, w, w,
    w, b, w, w, b, w, b, w,
    w, b, b, b, b, b, b, w,
    w, b, b, b, b, w, b, b,
    w, b, b, b, b, b, b, w,
    w, w, b, w, b, w, w, w,
    w, w, w, w, w, w, w, w]


def walk():
    for i in range(3):
        sense.set_pixels(cat1_pixels)
        sleep(0.5)
        sense.set_pixels(cat2_pixels)
        sleep(0.5)


sense.set_pixels(cat2_pixels)

while True:

    acceleration = sense.get_accelerometer_raw()

    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    f = math.sqrt(x**2 + y ** 2 + z ** 2)

    if f > 1:
        walk()
