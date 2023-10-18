from sense_hat import SenseHat
import time

sense = SenseHat()


p = [2, 3]
light_len = 3
space_size = 8
speed = 1/7

r = (255, 0, 0)
n = (0, 0, 0)
space = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    r, r, r, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]
# 24 --- 32
# p = 2 3
# p jobb oldala 3*8 + 2


def shift_right():
    sense.set_pixels(space)
    global r, n, p
    space[p[1]*8 + p[0] - 2] = n
    space[p[1]*8 + p[0] + 1] = r
    sense.set_pixels(space)
    p[0] = p[0] + 1


def shift_left():
    sense.set_pixels(space)
    global r, n, p
    space[p[1]*8 + p[0]] = n
    space[p[1]*8 + p[0] - 3] = r
    sense.set_pixels(space)
    p[0] = p[0] - 1


def main():

    global p
    while True:
        while True:
            shift_right()
            time.sleep(speed)
            if p[0] == space_size-1:
                break
        while True:
            shift_left()
            time.sleep(speed)
            if p[0] == light_len-1:
                break


main()
