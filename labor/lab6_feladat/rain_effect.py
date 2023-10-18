from sense_hat import SenseHat
import time
import random

sense = SenseHat()
b = (0, 0, 255)
n = (255, 255, 255)

space = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]

sense.set_pixels(space)

while True:
    global j
    random_blue = random.randint(0, 7)
    space[random_blue] = b
    sense.set_pixels(space)
    for i in range(56, 64):
        space[i] = space[i-8]
    for i in range(48, 56):
        space[i] = space[i-8]
    for i in range(40, 48):
        space[i] = space[i-8]
    for i in range(32, 40):
        space[i] = space[i-8]
    for i in range(24, 32):
        space[i] = space[i-8]
    for i in range(16, 24):
        space[i] = space[i-8]
    for i in range(8, 16):
        space[i] = space[i-8]
    for i in range(8):
        space[i] = n
    time.sleep(0.5)
    sense.set_pixels(space)
