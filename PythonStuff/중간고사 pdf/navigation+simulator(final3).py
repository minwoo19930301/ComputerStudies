from turtle import *
import time

def graph():
    global graph
    graph = {1 : {2:1, 6:1}, 2 : {1:1, 3:1}, 3: {2:1,8:1,4:1}, 4:{3:1,5:1}, 5:{4:1,10:1},6:{1:1, 11:1}, 8:{3:1,13:1}, 10:{5:1,15:1}, 11:{6:1,12:1,16:1}, 12:{11:1,13:1}, 13:{12:1,8:1,14:1,18:1}, 14:{13:1,15:1}, 15:{14:1,10:1,20:1}, 16:{11:1,21:1}, 18:{13:1,23:1}, 20:{15:1,25:1},21:{16:1,22:1}, 22:{21:1,23:1}, 23:{22:1,24:1}, 24:{23:1,25:1}, 25:{24:1,20:1}}
    
def graph_trafficlight():
    global graph, start
    distance, previous = dijkstra(graph, start) #to get closest approach to traffic light
    traffic_light=[1,3,5,11,13,15,21,23,25] #traffic light - area numbers
    for area in traffic_light:
        if start==area:
            for v in graph[area].keys():
                graph[area][v]=1
        else:
            for v in graph[area].keys():
                if (int(time.strftime("%S"))+v)%3==0:            #considering the moment when the algorithm opens 
                        graph[area][v]=1+(distance[area]%3)  #considering the delay time of each traffic light
                elif (int(time.strftime("%S"))+v)%3==1:
                        graph[area][v]=1+(distance[area]%3+1)
                else:
                        graph[area][v]=1+(distance[area]%3+2)
    return graph 
          
def dijkstra(graph, start):
    queue = {} #temporary memory
    distance = {}
    previous = {}
    
    for v in graph:
        distance[v] = 9999 #temporary infinite 
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



start=int(input("Enter the area number: "))
end= int(input("Input an end: "))
graph()
distance, previous = dijkstra(graph, start)

s=input("Navigate considering traffic?(y/n): ").lower()
if s == "y":  
    distance, previous = dijkstra(graph_trafficlight(), start)
else:
    pass
simulator(paths(start,end))
