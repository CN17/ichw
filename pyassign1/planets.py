#!/usr/bin/env python3

"""planets.py: This project imitates the running of planets in the Solar System.

__author__ = "Norman Cheng"
__pkuid__  = "1700011727"
__email__  = "1700011727@pku.edu.cn"
"""

import turtle
import threading
import math

sun = turtle.Turtle()
mercury = turtle.Turtle()
venus = turtle.Turtle()
earth = turtle.Turtle()
mars = turtle.Turtle()
jupiter = turtle.Turtle()
saturn = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor('white')
wn.screensize(1000,1000)

name = [sun,mercury,venus,earth,mars,jupiter,saturn]
colors = ['yellow','blue','light green','red','black','orange','light blue']

for i in range(7):
    name[i].color(colors[i])
    name[i].shape('circle')

def draw_a_sun(n):
    """draw a sun
    """
    n.dot(5)
    
def planets(n,a,b,s,x):
    """simulate the orbits of mercury
    """
    for i in range(1257):
        k = (i+1)*0.01
        x0 = math.cos(k)
        y0 = math.sin(k)
        if i == 0 :
            n.penup()
            n.speed(0)
        else:
            n.pendown()
            n.speed(s)
        n.goto((a*x0+x),(b*y0))  

def main():
    """main module
    """
    threads = []
    t1 = threading.Thread(target = draw_a_sun,args = (sun,))
    threads.append(t1)
    t2 = threading.Thread(target = planets,args = (mercury,50,45,10,0))
    threads.append(t2)
    t3 = threading.Thread(target = planets,args = (venus,90,80,7,-20))
    threads.append(t3)
    t4 = threading.Thread(target = planets,args = (earth,140,130,5,-40))
    threads.append(t4)
    t5 = threading.Thread(target = planets,args = (mars,140,100,3,20))
    threads.append(t5)
    t6 = threading.Thread(target = planets,args = (jupiter,150,60,2,60))
    threads.append(t6)
    t7 = threading.Thread(target = planets,args = (saturn,170,150,2,60))
    threads.append(t7)
    
    for t in threads:
        t.setDaemon(True)
        t.start()
    wn.exitonclick()
    
if __name__ == '__main__':
    main()
