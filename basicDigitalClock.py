import time 
import datetime as dt 
import turtle 

t = turtle.Turtle()# a turtle to display time 
t1 = turtle.Turtle() # turtle to create rectangle box
s = turtle.Screen() # screen
s.bgcolor("blue") # setting background colour

# obtaining time from system 
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour 

t1.pensize(3) 
t1.color("black")
t1.penup()

# set the position of turtle 
t1.goto(-20, 0)
t1.pendown()

# create rectangular box
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

t1.hideturtle() # hiding the turtle

while True:
    t.hideturtle()
    t.clear()
    # display time 
    t.write(str(hr).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2), 
            font = ("Aerial Narrow", 35, "bold"))
    
    time.sleep(1)
    sec += 1
    
    if sec == 60:
        sec = 0
        min += 1
    if min == 60:
        min = 0
        hr += 1
    if hr == 13:
        hr = 1