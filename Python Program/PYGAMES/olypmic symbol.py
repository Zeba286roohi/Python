#Program to draw the Olympic sign in Python Turtle  
#Importing Turtle  
import turtle   
ttl = turtle.Turtle()  

ttl.pensize(6)  
  
#creating the first or blue ring  
ttl.color('blue')  
ttl.penup()  
ttl.goto(-100,-25)  
ttl.pendown()  
ttl.circle(51)  
  
#creating the second or black ring  
ttl.color('black')  
ttl.penup()   
ttl.goto(10,-25)  
ttl.pendown()   
ttl.circle(51)  
  
#creating the third or red ring  
ttl.color('red')  
ttl.penup()  
ttl.goto(120,-25)  
ttl.pendown()    
ttl.circle(51)  
  
#creating the fourth or yellow ring  
ttl.color('yellow')  
ttl.penup()  
ttl.goto(-45,-75)  
ttl.pendown()  
ttl.circle(51)  
  
  
#creating the fifth or green ring  
ttl.color('green')  
ttl.penup()  
ttl.goto(65,-75)  
ttl.pendown()  
ttl.circle(51)  
ttl.hideturtle()  
ttl.done()  
