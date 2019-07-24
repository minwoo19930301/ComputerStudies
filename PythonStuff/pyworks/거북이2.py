import turtle
import ran
turtle.shape('turtle')
turtle.hideturtle()
turtle.speed(50)
turtle.shapesize(3,3,3)
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.left(90)
turtle.circle(200)
turtle.penup()
turtle.goto(0,0)
turtle.showturtle()
turtle.speed(3)
while True:
	turtle.right(random.randint(1,180))
	turtle.forward(50)
	if turtle.distance(0,0)>=150:
	    turtle.undo()
	turtle.left(random.randint(1,180))
	turtle.forward(50)
	if turtle.distance(0,0)>=150:
	    turtle.undo()
	
