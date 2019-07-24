import turtle
import random
turtle.shape('turtle')
turtle.shapesize(3,3,3)
turtle.penup()
turtle.forward(400)
turtle.pendown()
turtle.left(90)
turtle.circle(400)
turtle.penup()
turtle.goto(0,0)
while turtle.distance(0,0)<400:
	turtle.left(random.randint(1,180))
	turtle.forward(100)
	if turtle.distance(0,0)>=400:
		turtle.undo()
		