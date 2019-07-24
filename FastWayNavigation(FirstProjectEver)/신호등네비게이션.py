#2014311710 Kim Minwoo
from turtle import *
import time

def graph():
    global graph
    graph = {1 : {2:1, 6:1}, 2 : {1:1, 3:1}, 3: {2:1,8:1,4:1}, 4:{3:1,5:1}, 5:{4:1,10:1},6:{1:1, 11:1}, 8:{3:1,13:1}, 10:{5:1,15:1}, 11:{6:1,12:1,16:1}, 12:{11:1,13:1}, 13:{12:1,8:1,14:1,18:1}, 14:{13:1,15:1}, 15:{14:1,10:1,20:1}, 16:{11:1,21:1}, 18:{13:1,23:1}, 20:{15:1,25:1},21:{16:1,22:1}, 22:{21:1,23:1}, 23:{22:1,24:1}, 24:{23:1,25:1}, 25:{24:1,20:1}}
    
def graph_trafficlight():
    global graph, start
    distance, previous = dijkstra(graph, start) #to get closest approach(distance[x]) to traffic light
    traffic_light=[1,3,5,11,13,15,21,23,25] #traffic light - area numbers
    for area in traffic_light:
        if start==area:
            for v in graph[area].keys():
                graph[area][v]=1
        else:
            for v in graph[area].keys():
                if (int(time.strftime("%S"))+v)%3==0:            #considering the moment when the algorithm opens : pattern1
                        graph[area][v]=1+(distance[area]%3)  #distance[area] is the time that occurs to approach to traffic light    
                elif (int(time.strftime("%S"))+v)%3==1:         #pattern2    
                        graph[area][v]=1+(distance[area]%3+1)
                else:                                                      #pattern3
                        graph[area][v]=1+(distance[area]%3+2)
    return graph 
          
def dijkstra(graph, start):
    queue = {} #temporary memory
    distance = {}#distance from node to node
    previous = {}
    
    for v in graph:   #initialization
        distance[v] = 9999 #temporary "infinite" - distance from start to v is unknown 
        previous[v] = -1 #temporary "undefined" low number

        distance[start] = 0
        queue[v] = distance[v] 
        
    while queue :        
        u = pop_min(queue)
        
        for v in graph[u].keys(): 
            alt = distance[u] + graph[u][v]
            if (alt < distance[v]): # A shorter path to v has been found
                queue[v] = alt      # save
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
            path.append(end)     #Push vertex
            end=previous[end]   #traverse from target to source
        path.append(start)        #Push source
        path.reverse()
        return path


def simulator(paths):
    hideturtle()    #drawing paths
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
    plot=[]             #tinverting graph to turtle module
    for i in range(0,5):
        for j in range(0,5):
            plot.append((j*50,i*50))
    up()
    goto(plot[paths[0]-1])   #navigate
    down()
    shape("circle")
    showturtle()
    pencolor("red")
    speed(1)
    pensize(30)
    for k in paths:
        goto(plot[k-1])


start=int(input("Current area: "))
end= int(input("Final destination: "))
graph()
distance, previous = dijkstra(graph, start)     

s=input("Navigate considering traffic?(y/n): ").lower()
while (s!="y") or (s!="n"):
    if s == "y":  
        distance, previous = dijkstra(graph_trafficlight(), start)  #refreshing graph with traffics
        break
    elif s== "n":
        pass
        break
    else:
        s=input("Navigate considering traffic?(y/n): ").lower()
simulator(paths(start,end))
