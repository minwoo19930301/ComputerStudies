#2014311710 Kim Minwoo

import turtle
percentage=[7.6, 5.0, 4.7, 2.8, 2.8]

def main():
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(100)
    for i in range(5):
        drawRectangle(t,-293+80*i,0,80,percentage[i]*20)
    writeText(t)
    
def writeText(t):
    majors =["Biology\n(general)", "Nursing", "Psychology", "Mechanical\nEngineering", "Bus. Admin.\n   (general)"]
    t.pencolor("black")
    t.up()
    for i in range(5):
                 t.goto(-250+80*i, percentage[i]*20)
                 t.write(str(percentage[i])+"%", align="center", font=("Arial",10,"normal"))
                 t.goto(-250+80*i,10)
                 t.write(majors[i], align="center", font=("Arial",10,"normal"))
    t.goto(-290,-25)
    t.write("Most Popular Majors for College Freshmen in Fall 2013")

def drawRectangle(t,x,y,w,h,colorP="black",colorF="light blue"):
	t.pencolor(colorP)
	t.fillcolor(colorF)
	t.up()
	t.goto(x,y)
	t.down()
	t.begin_fill()
	for i in range(2):
		t.forward(w)
		t.left(90)
		t.forward(h)
		t.left(90)
	t.end_fill()





main()

