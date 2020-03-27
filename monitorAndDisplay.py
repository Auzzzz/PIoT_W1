
import json
import time
import random
from sense_hat import SenseHat

# https://pythonbasics.org/read-json-file/
# https://pythonhosted.org/sense-hat/api/


# JSON read
with open('config.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

# JSON test print
#print("cold_max: " + str(obj['cold_max']))
#print("comfortable_min: " + str(obj['comfortable_min']))
#print("comfortable_max: " + str(obj['comfortable_max']))

#declare temps
cold = (int(obj['cold_max']))
cmin = (int(obj['comfortable_min']))
cmax = (int(obj['comfortable_max']))
hot = (int(obj['hot_min']))
sense = SenseHat()

#colours
blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)
temp = sense.get_temperature()

def displaytemp():
    t = int(round(temp))
    if t < 10:
        #print("its cold")
        sense.clear(blue)
    elif t in range(cmin,cmax):
        #print("Compfhy ")
        sense.clear(yellow)
    elif t >= 23:
        #print("HOT")
        sense.clear(red)
    else:
        #print("error")
        sense.clear(green)




count = 0
while True:
    displaytemp()
    time.sleep(10)
    count +1
    #demo
    print(temp)
    #temp = random.randint(5,25)
        


# sense.clear(255,255,0)

# Text display not needed =(
#sense.show_message("Temp = %s C " % temp)
