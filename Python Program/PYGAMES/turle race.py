import turtle
import random

# Create the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtles
turtle1 = turtle.Turtle()
turtle1.color("green")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-150, 100)

turtle2 = turtle.Turtle()
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-150, 50)

turtle3 = turtle.Turtle()
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-150, 0)

# Create the finish line
finish_line = turtle.Turtle()
finish_line.color("black")
finish_line.pensize(5)
finish_line.penup()
finish_line.goto(150,150)
finish_line.pendown()
finish_line.goto(150,-150)
finish_line.hideturtle()

# Move the turtles
while True:
    turtle1.forward(random.randint(1,5))
    turtle2.forward(random.randint(1,5))
    turtle3.forward(random.randint(1,5))

    # Check for a winner
    if turtle1.xcor() >= 150:
        turtle1.write("I WON!",align="center", font=("Arial", 24, "normal"))
        break
    if turtle2.xcor() >= 150:
        turtle2.write("I WON!",align="center", font=("Arial", 24, "normal"))
        break
    if turtle3.xcor() >= 150:
        turtle3.write("I WON!",align="center", font=("Arial", 24, "normal"))
        break

turtle.exitonclick()
