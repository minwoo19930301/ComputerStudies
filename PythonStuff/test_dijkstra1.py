def dijkstra(graph, start):
    # Using priority queue to keep track of minium distance from start
    # to a vertex.
    pqueue = {} # vertex: distance to start
    dist = {}   # vertex: distance to start
    pred = {}   # vertex: previous (predecesor) vertex in shortest path
    
    # initializing dictionaries
    for v in graph:
        dist[v] = 9999 #9999 is a temporary value big enough to an unmeasured distance
        pred[v] = -1 #-1 is an initial value smaller than any integral or zero
        dist[start] = 0
        pqueue[v] = dist[v] # equivalent to push into queue
    while pqueue:
        u = popmin(pqueue) # for priority queues, pop will get the element with smallest value
        print(u)
        print(graph[u].keys())
        for v in graph[u].keys(): # for each neighbor of u
            print(v)
            newdist = dist[u] + graph[u][v] # distance u to v
            print(newdist)
            print()
            if (newdist < dist[v]): # is new distance shorter than one in dist?
                # found new shorter distance. save it
                pqueue[v] = newdist
                dist[v] = newdist
                pred[v] = u
 
    return dist, pred
 
def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    
    lowest= 9999    
    keyLowest = ''
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keyLowest = key
    del pqueue[keyLowest]
    print(pqueue)
    return keyLowest


graph = {0 : {1:6, 2:8},         
1 : {4:11},
2 : {3: 9},
3 : {},
4 : {5:3},
5 : {2: 7, 3:4}}
 
dist, pred = dijkstra(graph, 0)
print(pred)
print(dist)
print ("Predecesors in shortest path:")
for v in pred: print ("%s: %s" % (v, pred[v]))
print ("Shortest distance from each vertex:")
for v in dist: print ("%s: %s" % (v, dist[v]))
 
