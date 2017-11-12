# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
nodes = []
nodesd = {}
current_node = 0
def add_node(x,y):
    global current_node
    global nodesd
    global nodes
    current_node += 1
    nodes.append(current_node)
    nodesd[current_node] = [x,y]

distances = {}
def caldistance():
    global current_node
    global nodesd
    global distances
    for n in range(1,current_node+1):
        distances[n] = {}
        for m in range(1,current_node+1):
            if n == m:
                continue
            else:
                dis = (nodesd[m][0]-nodesd[n][0])**2 + (nodesd[m][1]-nodesd[n][1])**2
                distances[n][m] = math.sqrt(dis)

while True:
    print("input a node")
    x = int(input("x:"))
    y = int(input("y:"))
    add_node(x,y)
    plt.scatter(x,y)
    d = str(raw_input("Another one?[Y/n]"))
    if (d == "Y" or d == "y" or d == ""):
        continue
    else:
        break

caldistance()
#above
unvisited = {node: None for node in nodes}
visited = {}
current = 1
seq = []
line = []
a = []
b = []
currentDistance = 0
unvisited[current] = currentDistance
while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited:
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    seq.append(current)
    line.append(nodesd[current])
    a.append(nodesd[current][0])
    b.append(nodesd[current][1])
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

##dissum = 0
##nodeseq=[]
##for v in visited:
##    nodeseq.append(v)
##    dissum += visited[v]
print("Visit the nodes in the following sequence:")
print(seq)
print("The total distance is:")
print(newDistance)
print(line)
print(a)
print(b)
plt.plot(a,b)

plt.show()
