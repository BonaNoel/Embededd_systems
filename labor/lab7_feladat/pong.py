from sense_hat import SenseHat
import random
from time import sleep


sense = SenseHat()
speed = 0.4
basket = [7, 4]

w = (0, 0, 0)
r = (255, 0, 0)
b = (0, 0, 255)
game_space = [w, w, w, w, w, w, w, w,
              w, w, w, w, w, w, w, w,
              w, w, w, w, w, w, w, w,
              w, w, w, w, w, w, w, w,
              w, w, w, w, w, w, w, w,
              w, w, w, w, w, w, w, w,
              w, w, w, w, w, w, w, w,
              w, w, w, b, b, w, w, w]


up_down = -1


def update_space(x, y, colour):
    # index element from coordinate
    p = 8*x+y
    game_space[p] = colour
    sense.set_pixels(game_space)


def left(event):
    if event.action == 'pressed':
        # the basket reached the left side
        if basket[0] - 1 == 0:
            pass
        # move basket one position left
        else:
            update_space(basket[0], basket[1], w)
            basket[1] -= 1
            update_space(basket[0], basket[1] - 1, b)


def right(event):
    if event.action == 'pressed':
        # the basket reached the right side
        if basket[1] + 1 == 8:
            pass
        # move basket one position left
        else:
            update_space(basket[0], basket[1] - 1, w)
            basket[1] += 1
            update_space(basket[0], basket[1], b)


sense.stick.direction_left = left
sense.stick.direction_right = right


sense.clear()
sense.set_pixels(game_space)
game_alive = True
score = 0


while game_alive:
    x = 1
    y = random.randint(0, 7)
    d = random.choice([-1, 1])
    update_space(x, y, r)

    while True:
        sleep(speed)
        update_space(x, y, w)
        # ball is on the edge of x dimension

        if x == 7:
            if y == basket[1] - 1 or y == basket[1]:
                # ball is in the basket
                score += 1
                up_down = 1
                d = random.choice([-1, 1])
            else:
                # ball is out of the space
                game_alive = False
                break
        update_space(basket[0], basket[1], b)
        # ball reached the right side of the space
        if y == 7 and d == 1:
            d = -1
        # ball reached the left side of the space
        elif y == 0 and d == -1:
            d = 1
        # ball reached the top of the space
        if x == 0:
            up_down = -1

        y += d
        if up_down == -1:
            x += 1
        else:
            x -= 1
        update_space(x, y, r)


sense.clear()
sense.show_message("Game over!", scroll_speed=0.05, back_colour=w)
sense.show_message("Score: " + str(score), scroll_speed=0.02, back_colour=w)
