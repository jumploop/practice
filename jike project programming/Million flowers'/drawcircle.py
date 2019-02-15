#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import turtle


# draw the circle using turtle
def drawCircleTurtle(x, y, r):
    # move to the start of circle
    turtle.setup()
    turtle.setpos(x + r, y)
    turtle.down()

    # draw the circle
    for i in range(0, 365, 5):
        a = math.radians(1)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


# drawCircleTurtle(100,100,50)
# turtle.mainloop()
from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
