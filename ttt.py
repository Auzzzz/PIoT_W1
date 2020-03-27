
from sense_hat import SenseHat
import random
import time

sense = SenseHat()
sense.show_message("AA", scroll_speed=0.06)
time.sleep(3)

replies = ['1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8'
        ]

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1.6 or y > 1.6 or z > 1.6 :
        sense.show_message(choice(replies))
    else:
        sense.clear()
