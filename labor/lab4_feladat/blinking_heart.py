from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

x = (255, 0, 0)
# red
w = (255, 255, 255)
# white

heart_pixels = [
    w, w, w, w, w, w, w, w,
    w, x, x, w, w, x, x, w,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    w, x, x, x, x, x, x, w,
    w, w, x, x, x, x, w, w,
    w, w, w, x, x, w, w, w,
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
                for i in range(3):
                    sense.set_pixels(heart_pixels)
                    sleep(0.5)
                    sense.clear(255, 255, 255)
                    sleep(0.5)
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
