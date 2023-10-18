from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()

SCORE = 0
FOOD = 0
GAME_OVER = 0
INVINCIBLE = 0
RERUN = 0

WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

evett = False

speed = 0.4
snakeX = [1]
snakeY = [3]
MovX = 1
MovY = 0

sense.clear()

while True:

    if GAME_OVER:
        break

    # spawn food
    if FOOD == 0:
        food = [random.randint(1, 6), random.randint(1, 6)]
        FOOD = 1

    for i in range(len(snakeX)):
        if snakeX[i] == food[0] and snakeY[i] == food[1]:
            FOOD = 0
            RERUN = 1

    if RERUN == 1:
        RERUN = 0
        continue

    # reach border game over
    if snakeX[0] <= 0 or snakeX[0] >= 7 or snakeY[0] <= 0 or snakeY[0] >= 7:
        GAME_OVER = 1
        continue

    # reach snake body game over
    if INVINCIBLE == 0:
        for i in range(1, len(snakeX)):
            if snakeX[0] == snakeX[i] and snakeY[0] == snakeY[i]:
                GAME_OVER = 1

    INVINCIBLE = 0
    if snakeX[0] == food[0] and snakeY[0] == food[1]:
        evett = True

    # eat food +1 score + 1 new snake element
    if evett:
        print("eat")
        FOOD = 0
        SCORE = SCORE + 1
        INVINCIBLE = 1
        snakeX.append(snakeX[-1])
        snakeY.append(snakeY[-1])

    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'up':
                MovX = 0
                MovY = -1
            elif event.direction == 'down':
                MovX = 0
                MovY = +1
            elif event.direction == 'left':
                MovX = -1
                MovY = 0
            elif event.direction == 'right':
                MovX = 1
                MovY = 0

    snakeX[0] += MovX
    snakeY[0] += MovY

    # move snake
    for i in range(len(snakeX) - 1, 0, -1):
        snakeX[i] = snakeX[i - 1]
        snakeY[i] = snakeY[i - 1]

    print("snakeX: " + str(snakeX[0]) + " snakeY: " + str(snakeY[0]))
    print("foodX: " + str(food[0]) + " foodY: " + str(food[1]))
    print("")
    # show movement and food
    sense.clear()
    sense.set_pixel(food[0], food[1], RED)
    for i in range(len(snakeX)):
        sense.set_pixel(snakeX[i], snakeY[i], GREEN)

    sleep(speed)


sense.show_message("Game Over", text_colour=RED)
sense.show_message("Score: " + str(SCORE), text_colour=RED)
