#Program to draw a Rainbow using turtle in Python  
# Importing the turtle package  
import turtle    
scr = turtle.Screen()  
ttl = turtle.Turtle()  
  
def semi_circle(clr, rad, val):  
  
    ttl.color(clr)  
    ttl.circle(rad, -180)  
    ttl.up()  
  
    # Moving the turtle to a given position/coordinates  
    ttl.setpos(val, 0)  
    ttl.down()  
    ttl.right(180)  
  
  
# Setting the colors for drawing the Rainbow  
clr = ['violet', 'indigo', 'blue',  
    'green', 'yellow', 'orange', 'red']   
scr.setup(800, 600)   
scr.bgcolor('black')  
  
# Setting the various turtle features  
ttl.right(90)  
ttl.width(11)  
ttl.speed(8)  
  
# for loop to draw 7 semicircles  
for j in range(7):  
    semi_circle(clr[j], 10*(  
    j + 8), -10*(j + 1))   
ttl.hideturtle()  
