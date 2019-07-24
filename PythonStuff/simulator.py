from turtle import *

path=[1,3,23]

def simulator():
    hideturtle()
    speed(0)
    pencolor("gray")
    pensize(50)
    for i in range(4):
        forward(200)
        left(90)
    goto(0,100)
    goto(200,100)
    up()
    goto(100,200)
    down()
    goto(100,0)
    goto(0,0)
    shape("circle")
    showturtle()
    pencolor("red")
    speed(1)
    pensize(30)
    plot={1:(0, 0), 2:(50, 0), 3:(100, 0), 4:(150, 0), 5:(200, 0), 6:(0, 50), 7:(50, 50), 8:(100, 50), 9:(150, 50), 10:(200, 50), 11:(0, 100), 12:(50, 100), 13:(100, 100), 14:(150, 100),
    15:(200, 100), 16:(0, 150), 17:(50, 150), 18:(100, 150), 19:(150, 150), 20:(200, 150), 21:(0, 200), 22:(50, 200), 23:(100, 200), 24:(150, 200), 25:(200, 200)}
    for k in path:
        goto(plot.get(k))
    
simulator()


