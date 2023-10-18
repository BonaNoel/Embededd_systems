from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

x = (255, 0, 0)
# red
w = (255, 255, 255)
# white
up_pixels = [
    w, w, w, w, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, x, x, x, w, w, w,
    w, x, w, x, w, x, w, w,
    w, w, w, x, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, w, w, w, w, w, w]


down_pixels = [
    w, w, w, w, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, x, w, x, w, x, w, w,
    w, w, x, x, x, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, w, w, w, w, w, w]

left_pixels = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, x, w, w, w, w, w,
    w, x, x, x, x, x, x, w,
    w, w, x, w, w, w, w, w,
    w, w, w, x, w, w, w, w,
    w, w, w, w, w, w, w, w]

right_pixels = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, x, w, w, w,
    w, w, w, w, w, x, w, w,
    w, x, x, x, x, x, x, w,
    w, w, w, w, w, x, w, w,
    w, w, w, w, x, w, w, w,
    w, w, w, w, w, w, w, w]

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                sense.set_pixels(up_pixels)
            elif event.direction == "down":
                sense.set_pixels(down_pixels)
            elif event.direction == "left":
                sense.set_pixels(left_pixels)
            elif event.direction == "right":
                sense.set_pixels(right_pixels)
            elif event.direction == "middle":
                sense.show_letter("M")

        sleep(0.5)
        sense.clear()
