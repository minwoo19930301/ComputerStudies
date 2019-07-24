def graph():
    global graph
    a=traffic_signal()
    graph ={1 : {2:1, 6:1}, 2 : {1:1, 3:1}, 3: {2:1,8:1,4:1}, 4:{3:1,5:1}, 5:{4:1,10:1},
            6:{1:1, 11:1}, 8:{3:1,13:1}, 10:{5:1,15:1}, 11:{6:1,12:1,16:1}, 12:{11:1,13:1}, 13:{12:1,8:1,14:1,18:1},
            14:{13:1,15:1}, 15:{14:1,10:1,20:1}, 16:{11:1,21:1}, 18:{13:1,23:1}, 20:{15:1,25:1},21:{16:1,22:1}, 22:{21:1,23:1},
            23:{22:1,24:1}, 24:{23:1,25:1}, 25:{24:1,20:1}}

    


def traffic_signal():
    red_light
    
    if%3==0:
        mode=red_light
    elif %3==1:
        mode=green_light
    elif %3==2:
        mode=left_turn

    
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
        time=1
        u = pop_min(queue) # for priority queues, pop will get the element with smallest value
        for v in graph[u].keys(): # for each neighbor of u
            w= graph[u][v] # distance u to v
            newdist = distance[u] + w
            if (newdist < distance[v]): # is new distance shorter than one in distance?
                # found new shorter distance. save it
                queue[v] = newdist
                distance[v] = newdist
                previous[v] = u
                time+=1
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



graph()
start=int(input("Enter the area number: "))
end= int(input("Input an end: "))

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
