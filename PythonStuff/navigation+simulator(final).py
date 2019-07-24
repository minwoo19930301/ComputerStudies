def graph():
    global graph
    n=input("Navigate considering traffic?(y/n): ").lower()
    if n == "y":
        a,b,c,d,e=randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)      #a,b,c,d,e are temporarily made traffics or traffic_lights. Recommeneded to match for interactioning objects
    if n == "n":
        a,b,c,d,e=0,0,0,0,0
    graph ={1 : {2:1, 6:1}, 2 : {1:1, 3:1}, 3: {2:a,8:a,4:a}, 4:{3:1,5:1}, 5:{4:1,10:1},
            6:{1:b, 11:b}, 8:{3:1,13:1+c}, 10:{5:1,15:1}, 11:{6:1,12:1,16:1}, 12:{11:1,13:1}, 13:{12:c,8:c,14:c,18:c},
            14:{13:1,15:1}, 15:{14:d,10:d,20:d}, 16:{11:1,21:1}, 18:{13:1,23:1}, 20:{15:1,25:1},21:{16:1,22:1}, 22:{21:1,23:1},
            23:{22:e,24:e}, 24:{23:1,25:1}, 25:{24:1,20:1}}
    

   
def dijkstra(graph, start):
    # Using priority queue to keep track of minium distance from start
    # to a vertex.
    queue = {} # vertex: distance to start
    distance = {}   # vertex: distance to start
    previous = {}   # vertex: previous (predecesor) vertex in shortest path
    # initializing dictionaries
    for v in graph:
        distance[v] = 9999 #9999 is a temporary value big enough to an unmeasured distance
        previous[v] = -1 #-1 is an initial value smaller than any integral or zero
        distance[start] = 0
        queue[v] = distance[v] # equivalent to push into queue
    while queue :        
        u = pop_min(queue) # for priority queues, pop will get the element with smallest value
        for v in graph[u].keys(): # for each neighbor of u
            w= graph[u][v] # distance u to v
            newdist = distance[u] + w
            if (newdist < distance[v]): # is new distance shorter than one in distance?
                # found new shorter distance. save it
                queue[v] = newdist
                distance[v] = newdist
                previous[v] = u
    return distance, previous
 
def pop_min(queue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    
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
    plot={1:(0, 0), 2:(50, 0), 3:(100, 0), 4:(150, 0), 5:(200, 0), 6:(0, 50), 7:(50, 50), 8:(100, 50), 9:(150, 50), 10:(200, 50), 11:(0, 100), 12:(50, 100), 13:(100, 100), 14:(150, 100),
    15:(200, 100), 16:(0, 150), 17:(50, 150), 18:(100, 150), 19:(150, 150), 20:(200, 150), 21:(0, 200), 22:(50, 200), 23:(100, 200), 24:(150, 200), 25:(200, 200)}
    up()
    goto(plot[paths[0]])
    down()
    shape("circle")
    showturtle()
    pencolor("red")
    speed(1)
    pensize(30)
    for k in paths:
        goto(plot.get(k))

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


print(paths(start,end))

print ("Shortest path length:")
for v in distance:
    if v==start:
        continue
    print ("%s: %s" % (v, distance[v]))

print(distance)
simulator(paths(start,end))
