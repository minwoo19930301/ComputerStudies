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
while True:
	random.choice([1,2])
	if random.choice([1,2]) = 1:
			turtle.right(random.randint(1,180))
			turtle.forward(100)
			if turtle.distance(0,0)>=400:
				turtle.undo()
	if random.choice([1,2]) = 2:
			turtle.left(random.randint(1,180))
			turtle.forward(100)
			if turtle.distance(0,0)>=400:
				turtle.undo()
	