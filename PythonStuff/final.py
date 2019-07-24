def simulator(paths):
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
    plot=[]
    for i in range(0,5):
        for j in range(0,5):
            plot.append((j*50,i*50))
    up()
    goto(plot[paths[0]-1])
    down()
    shape("circle")
    showturtle()
    pencolor("red")
    speed(1)
    pensize(30)
    for k in paths:
        goto(plot[k-1])