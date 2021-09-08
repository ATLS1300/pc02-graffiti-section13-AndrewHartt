#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Andrew Hart
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.home()
turtle.penup()
turtle.color("OrangeRed")
turtle.right(90)
turtle.forward(85)
turtle.left(90)
turtle.forward(110)
turtle.pendown()
turtle.forward(100)
turtle.color("black")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward (80)
turtle.right (90)
turtle.forward(100)
turtle.right(90)
turtle.forward(80)
turtle.end_fill()
turtle.penup()
turtle.home()
turtle.pendown()
turtle.pensize(8)
turtle.color("cyan")
turtle.circle(120)
turtle.left(90)
turtle.penup()
turtle.forward(60)
turtle.right(90)
turtle.forward(25)
turtle.pendown()
turtle.pensize(1)
turtle.color("red")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.penup()
turtle.home()
turtle.right(90)
turtle.forward(85)
turtle.left(90)
turtle.forward(235)
turtle.pendown()
turtle.color("royal blue")
turtle.begin_fill()
turtle.forward(20)
turtle.right(72)
turtle.forward(20)
turtle.right(72)
turtle.forward(20)
turtle.right(72)
turtle.forward(20)
turtle.right(72)
turtle.forward(20)
turtle.end_fill()
turtle.penup()
turtle.forward(40)
turtle.right(90)
turtle.forward(40)
turtle.pendown()
turtle.color("green")
turtle.pensize(3)
turtle.forward(20)
turtle.right(60)
turtle.forward(20)
turtle.right(60)
turtle.forward(20)
turtle.right(60)
turtle.forward(20)
turtle.right(60)
turtle.forward(20)
turtle.right(60)
turtle.forward(20)
turtle.penup()
turtle.home()




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
