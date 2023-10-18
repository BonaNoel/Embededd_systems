from sense_hat import SenseHat
from time import sleep
import math

sense = SenseHat()


def switch(z):
    if z == 0:
        print("Bad Z result")

    elif z == 1:
        print("Settled Fine")
    elif z == 2:
        print("Fine Weather")
    elif z == 3:
        print("Fine, Becoming Less Settled")
    elif z == 4:
        print("Fairly Fine, Showery Later")
    elif z == 5:
        print("Showery, Becoming More Unsettled")
    elif z == 6:
        print('Unsettled, Rain Later')
    elif z == 7:
        print('Rain at Times, Worse Later')
    elif z == 8:
        print('Rain at Times, Becoming Very Unsettled')
    elif z == 9:
        print('Very Unsettled, Rain')

    elif z == 10:
        print('Settled Fine')
    elif z == 11:
        print('Fine Weather')
    elif z == 12:
        print('Fine, Possibly Showers')
    elif z == 13:
        print('Fairly Fine, Showers Likely')
    elif z == 14:
        print('Showery, Bright Intervals')
    elif z == 15:
        print('Changeable, Some Rain')
    elif z == 16:
        print('Unsettled, Rain at Times')
    elif z == 17:
        print('Rain at Frequent Intervals')
    elif z == 18:
        print('Very Unsettled, Rain')

    elif z == 20:
        print('Settled Fine')
    elif z == 21:
        print('Fine Weather')
    elif z == 22:
        print('Becoming Fine')
    elif z == 23:
        print('Fairly Fine, Improving')
    elif z == 24:
        print('Fairly Fine, Possibly Showers Early')
    elif z == 25:
        print('Showery Early, Improving')
    elif z == 26:
        print('Changeable, Mending')
    elif z == 27:
        print('Rather Unsettled, Clearing Later')
    elif z == 28:
        print('Unsettled, Probably Improving')
    elif z == 29:
        print('Unsettled, Short Fine Intervals')
    elif z == 30:
        print('Very Unsettled, Finer at Times')
    elif z == 31:
        print('Stormy, Possibly Improving')
    elif z == 32:
        print('Stormy, Much Rain')

    else:
        print("Bad Z result")


while True:
    t = sense.get_temperature()
    p1 = sense.get_pressure()  # 1 millibars = 1 hpa
    h = sense.get_humidity()

    p0 = p1 * (1-((0.0065*125)/(t + 0.0065 * h + 273.15)))**(-5.257)

    sleep(5)

    p2 = sense.get_pressure()

    # falling 1 stable 2 rising 3
    pdiffrence = p2 - p1

    if pdiffrence <= -1.6:
        state = 1
    elif pdiffrence > -1.6 and pdiffrence < 1.6:
        state = 2
    else:
        state = 3

    z = 0

    if state == 1 and 985 <= p0 and p0 <= 1050:
        z = 127 - 0.12*p0
    elif state == 2 and 960 <= p0 and p0 < 1033:
        z = 144 - 0.13*p0
    elif state == 3 and 947 <= p0 and p0 <= 1030:
        z = 185 - 0.16*p0

    z = math.floor(z)
    switch(z)
