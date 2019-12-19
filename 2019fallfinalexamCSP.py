#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name Sha'Quan Logan
#
#Date 12/19/19
#


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl
import random as random
#create turtle
drawer=trtl.Turtle()
drawer.shape("triangle")
drawer.color("black")
drawer.speed(00)
drawer.pendown()


#movement functions
def Up():
    drawer.setheading(90)
    drawer.forward(10)
def Down():
    drawer.setheading(270)
    drawer.forward(10)
def Right():
    drawer.setheading(00)
    drawer.forward(10)
def Left():
    drawer.setheading(180)
    drawer.forward(10)


#color/drawing functions
def pencolor():
    drawer.color("red")
def pencolor():
    drawer.color("yellow")
def pencolor():
    drawer.color("blue")


#create screen

#bind to keypresses
def O():
    drawer.pensize (50)
def P():
    drawer.pensize(100)
#listen


#mainloop
wn = trtl.Screen()   
wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.onkeypress(Right,"Right")
wn.onkeypress(Left,"Left")


wn.onkeypress(O)
wn.onkeypress(P)

wn.listen()
wn.mainloop()