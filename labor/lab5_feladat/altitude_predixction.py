from sense_hat import SenseHat

sense = SenseHat()

p = sense.get_pressure()
p0 = 1013.25


h = 44331 * (1-(p / p0)**(1/5.2558))

h = round(h)

h = str(h) + ' m'

print(h)
