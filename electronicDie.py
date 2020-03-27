
#https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8
from sense_hat import SenseHat
import time
import random

sense = SenseHat()
count = 0
number = 0

def dice():
	x, y, z = sense.get_accelerometer_raw().values()

	x = abs(x)
	y = abs(y)
	z = abs(z)

	if x > 2 or y > 2 or z > 2:
		number = random.randint(1,6)

		print(number)

while True:
	dice()
	sense.show_message(str(number))
	sense.clear()
	time.sleep(2)
	count +1

	#x=round(x, 0)
	#y=round(y, 0)
	#z=round(z, 0)
	#print("x={0}, y={1}, z={2}".format(x, y, z))

