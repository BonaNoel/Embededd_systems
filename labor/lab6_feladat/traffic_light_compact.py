from sense_hat import SenseHat
import time


sense = SenseHat()

state = 0

w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
y = (255, 255, 0)
n = (0, 0, 0)

red = [
    n, n, n, r, r, n, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]

red_yellow = [
    n, n, n, r, r, n, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]

yellow = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]

green = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, g, g, n, n, n,
    n, n, n, g, g, n, n, n
]


def normal_state(color, duration):
    sense.set_pixels(color)
    time.sleep(duration)
    sense.clear()


def out_of_order_state():
    sense.set_pixels(yellow)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)


def set_state():
    global state
    # state variable has been defined outside
    if state < 3:
        state += 1
    elif state == 3:
        state = 0
    else:
        pass


def button_event(event):
    global state
    if event.action == 'released':
        if state != 4:
            state = 4
        else:
            state = 3


sense.stick.direction_middle = button_event


def main():
    global state
    while True:
        if state == 0:
            normal_state(red, 3)
        elif state == 1:
            normal_state(red_yellow, 1)
        elif state == 2:
            normal_state(green, 2)
        elif state == 3:
            normal_state(yellow, 1)
        else:
            out_of_order_state()
        set_state()


main()
