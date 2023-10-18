from sense_hat import SenseHat
import time
import matplotlib.pyplot as plt
import math

sense = SenseHat()

calibration = True


def stop():
    global calibration
    calibration = False


def plot(filename):
    # define two lists
    x_list = []
    y_list = []

    try:
        # open the file for read
        file = open(filename, 'r')
        # break file content into lines
        lines = file.readlines()
        # go through all lines
        for line in lines:
            values = line.split(',')
            x_list.append(float(values[0]))
            y_list.append(float(values[1]))
    finally:
        file.close()

    # max-min values
    xmax = max(x_list)
    xmin = min(x_list)
    ymax = max(y_list)
    ymin = min(y_list)
    print('Max x: ', xmax, 'Min x: ', xmin)
    print('Max y: ', ymax, 'Min y: ', ymin)
    # create graph

    line1, = plt.plot(range(1, len(x_list) + 1), x_list, 'r-', label='x')
    line2, = plt.plot(range(1, len(y_list) + 1), y_list, 'b--', label='y')
    plt.xlabel('Measurements')
    plt.ylabel('Value')
    plt.legend(handles=[line1, line2])
    plt.show()
    return xmax, xmin, ymax, ymin


def main():
    sense = SenseHat()
    filename = 'compass.txt'
    # open file for write (rewrite its content)
    file = open(filename, 'w')
    sense.stick.direction_middle = stop
    print('Start data acquisition…')
    # calibration process
    while calibration:
        magnet = sense.get_compass_raw()
        x = magnet['x']
        y = magnet['y']
        file.wtite(str(x) + ',' + str(y) + '\n')
    file.close()
    xmax, xmin, ymax, ymin = plot(filename)

    while True:
        magnet = sense.get_compass_raw()
        x = magnet['x']
        y = magnet['y']

        # range transform
        xz = -1 + ((1-(-1)) / (xmax - xmin)) * (x - xmin)
        yz = -1 + ((1-(-1)) / (ymax - ymin)) * (y - ymin)

        # degree (a) calculation
        if xz == 0 and yz < 0:
            deg = 90
        elif xz == 0 and yz > 0:
            deg = 270
        elif yz < 0:
            deg = 360 + math.atan2(yz, xz) * (180/3.14159)
        else:
            deg = math.atan2(yz, xz) * (180/3.14159)

        # cardinal points
        if deg < 22.5 or deg > 337.5:
            sense.show_letter('N')
        elif deg < 67.5:
            sense.show_letter('NE')
        elif deg < 112.5:
            sense.show_letter('E')
        elif deg < 157.5:
            sense.show_letter('SE')
        elif deg < 202.5:
            sense.show_letter('S')
        elif deg < 247.5:
            sense.show_letter('SW')
        elif deg < 292.5:
            sense.show_letter('W')
        else:
            sense.show_letter('NW')

        time.sleep(0.2)

        sense.clear()
