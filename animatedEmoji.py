
from sense_hat import SenseHat
import time

sense = SenseHat()
set_pixels = True
R = [255, 0, 0]# Red
G = [0, 255, 0]# Green
B = [0, 0, 255]# Blue
Y = [255, 255, 0]# Yellow
X = [0, 0, 0]# Black
W = [255, 255, 255]# White

def question_mark():
 emoji = [
  W, W, W, R, R, W, W, W,
  W, W, R, W, W, R, W, W,
  W, W, W, W, W, R, W, W,
  W, W, W, W, R, W, W, W,
  W, W, W, R, W, W, W, W,
  W, W, W, R, W, W, W, W,
  W, W, W, W, W, W, W, W,
  R, W, W, R, W, W, W, W
 ]
 return emoji

def face():
 emoji = [
  X, X, X, Y, Y, X, X, X,
  X, X, Y, Y, Y, Y, X, X,
  X, Y, Y, Y, Y, Y, Y, X,
  Y, Y, Y, Y, Y, Y, Y, Y,
  Y, Y, Y, Y, Y, Y, Y, Y,
  X, Y, Y, Y, Y, Y, Y, X,
  X, X, Y, Y, Y, Y, X, X,
  X, X, X, Y, Y, X, X, X
 ]
 return emoji





display = [question_mark, face]
count = 0

while True:
    sense.set_pixels(display[count % len(display)]())
    time.sleep(3)
    count += 1
##https://pythonhosted.org/sense-hat/api/
