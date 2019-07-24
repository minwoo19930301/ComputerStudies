class Knoten(object):
  def __init__(self, name, connections=None):
    self.name = name
    self.connections = {}
    if connections is not None:
            self.connections.update(connections)

knoten=[
        Knoten("M", {"C":1,  "D":1}),
        Knoten("H", {"B":1}),
        Knoten("C", {"S":1,  "B":1}),
        Knoten("B", {"H":1,  "C":1}),
        Knoten("S", {"C":1})
]

def  shortest_path(start, end):
        P=dijsktra(start)
        path, node =[], end
        while (node != start):
            if path.count(node):break
            path.append(node)
            node=P[node]
        return [start] + list(reversed(path))
            

def dijsktra(start):
        D, P ={}, {}
        for knot in knoten:
                D[knot.name], P[knot.name] = float("inf"), None
        D[start]=0
        unseen_nodes = list(knoten)
        while unseen_nodes:
                shortest = min(unseen_nodes, key=lambda node:D[node.name])
                for neighbor, distance in shortest.connections.items():
                        if neighbor not in [node.name for node in unseen_nodes]:
                                continue
                        if D[shortest.name] + distance < D[neighbor]:
                                D[neighbor]=D[shortest.name] + distance
                                P[neighbor]=shortest.name

        return P

print("hi")
print(shortest_path("M","S"))
print("hi")
