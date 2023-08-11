import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Stylish Name Writing")

# Create a turtle for writing the name
name_turtle = turtle.Turtle()
name_turtle.speed(0)


# Function to write a stylish name
def write_stylish_name(name):
    name_turtle.goto(-150, 0)
    name_turtle.pendown()
    name_turtle.color("blue")
    name_turtle.pensize(2)
    
    for char in name:
        name_turtle.forward(20)
        name_turtle.write(char, font=("Comic SANS", 34, "bold"))
        name_turtle.forward(20)
        screen.update()
        time.sleep(0.5)  # Adjust the delay as needed

# Get user's name
user_name = input("Enter your name: ")

# Write the stylish name with animation
write_stylish_name(user_name)

# Close the window on click
screen.exitonclick()
