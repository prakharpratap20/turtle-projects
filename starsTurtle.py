import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # Set screen to full size
screen.bgcolor("black")
screen.title("Starry Night")

# Create a turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.hideturtle()

# Draw stars
def draw_stars():
    for _ in range(100):
        x = random.randint(-500, 500)
        y = random.randint(-350, 350)
        size = random.randint(1, 4)
        star_turtle.penup()
        star_turtle.goto(x, y)
        star_turtle.pendown()
        star_turtle.color("white")
        star_turtle.dot(size)

# Animate shooting stars
def animate_shooting_stars():
    for _ in range(20):
        x = random.randint(-500, 500)
        y = random.randint(-250, 250)
        length = random.randint(50, 100)
        angle = random.randint(160, 200)
        star_turtle.penup()
        star_turtle.goto(x, y)
        star_turtle.pendown()
        star_turtle.color("white")
        star_turtle.setheading(angle)
        star_turtle.forward(length)
        star_turtle.penup()

# Draw a moon
def draw_moon():
    star_turtle.penup()
    star_turtle.goto(-400, 250)
    star_turtle.pendown()
    star_turtle.color("white")
    star_turtle.begin_fill()
    star_turtle.circle(60)
    star_turtle.end_fill()

# Main loop
while True:
    star_turtle.clear()
    draw_stars()
    draw_moon()
    animate_shooting_stars()

    screen.update()
    turtle.delay(100)
