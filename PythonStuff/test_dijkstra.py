def graph():
    global graph
    graph ={0 : {1:1, 2:1,},
    1 : {0:1, 5: 1, 4: 1},
    2: {0:1},
    3:  {4:1},
    4 : {3:1, 1:1},
    5 : {1:1}}

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
        u = pop_min(queue)# for priority queues, pop will get the element with smallest value
        print(u)
        print(queue,"Que2")
        for v in graph[u].keys(): # for each neighbor of u
            w= graph[u][v] # distance u to v
            newdist = distance[u] + w
            print(newdist)
            print(previous,"PR")
            if (newdist < distance[v]): # is new distance shorter than one in distance?
                # found new shorter distance. save it
                queue[v] = newdist
                print(queue[v])
                distance[v] = newdist
                print(distance[v])
                previous[v] = u
                print(previous[v])
                print("......")
            print(previous,"PR2") 
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
            print(queue[key],"Q")
            lowest = queue[key]
            keyLowest = key
    print(keyLowest, "KL")
    del queue[keyLowest]
    print(queue,"Que")
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
