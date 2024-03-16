from turtle import *


#we want to paint a house

#step 1: draw a square
shape("turtle")
width(7)
speed(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70)
color("orange")
left(90)
forward(120)     #height forward
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(60)
forward(200)
left(120)
forward(200)
end_fill()








exitonclick()