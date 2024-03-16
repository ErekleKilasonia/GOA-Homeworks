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
begin_fill()
left(90)
forward(120)     #height forward
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()

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


color("blue")
begin_fill()
penup()
goto(60,120)
pendown()
right(150)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

color("blue")
begin_fill()
penup()
goto(140,120)
pendown()
right(270)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
penup()
goto(0,0)




exitonclick()