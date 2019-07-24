def graph():
    global graph
    n=input("Navigate considering traffic?(y/n): ").lower()
    if n == "y":
        a,b,c,d,e=randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)      #a,b,c,d,e are temporarily made traffics or traffic_lights. Recommeneded to match for interactioning objects
    if n == "n":
        a,b,c,d,e=1,1,1,1,1
    graph ={1 : {2:c, 6:c}, 2 : {1:1, 3:1}, 3: {2:a,8:a,4:a}, 4:{3:1,5:1}, 5:{4:b,10:b},
            6:{1:b, 11:b}, 8:{3:1,13:1+c}, 10:{5:1,15:1}, 11:{6:1,12:1,16:1}, 12:{11:1,13:1}, 13:{12:c,8:c,14:c,18:c},
            14:{13:1,15:1}, 15:{14:d,10:d,20:d}, 16:{11:1,21:1}, 18:{13:1,23:1}, 20:{15:1,25:1},21:{16:e,22:e}, 22:{21:1,23:1},
            23:{22:e,24:e}, 24:{23:1,25:1}, 25:{24:d,20:d}}
    

   
def dijkstra(graph, start):
    queue = {} 
    distance = {}   
    previous = {}
    
    for v in graph:
        distance[v] = 9999 
        previous[v] = -1 

        distance[start] = 0
        queue[v] = distance[v] 
        
    while queue :        
        u = pop_min(queue)
        
        for v in graph[u].keys(): 
            alt = distance[u] + graph[u][v]
            if (alt < distance[v]):
                queue[v] = alt
                distance[v] = alt
                previous[v] = u
    return distance, previous
 
def pop_min(queue):
    lowest= 9999    
    keyLowest = ''
    for key in queue:
        if queue[key] < lowest:
            lowest = queue[key]
            keyLowest = key
    del queue[keyLowest]
    return keyLowest

def paths (start, end):
        path=[]
        while end!=start:
            path.append(end)
            end=previous[end]
        path.append(start)
        path.reverse()
        return path


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

from random import *
from turtle import *

start=int(input("Enter the area number: "))
end= int(input("Input an end: "))
graph()
distance, previous = dijkstra(graph, start)
print ("Area before last move:")
for v in previous:
    if v==start:
        continue
    print ("%s: %s" % (v, previous[v]))

print ("Shortest path length:")
for v in distance:
    if v==start:
        continue
    print ("%s: %s" % (v, distance[v]))

simulator(paths(start,end))
