import argparse
import sys 

# def main(arguments):
def main():
    # filename = arguments[0]
    filename = "graf1.txt"
    with open(filename, 'r') as filehandle:
        data = filehandle.read()
    data = data.split()
    width = len(data[0])
    height = len(data)
    data = "".join(data)

    q = []
    for i in range(len(data)):
        q.append(Node(i, data[i], []))
    
    for i in range(len(q)):
        neighbours = []
        neigh = i+width
        if neigh < width*height:
            neighbours.append(neigh)
        neigh = i-width
        if neigh >= 0:
            neighbours.append(neigh)
        neigh = i+1
        if neigh//width == i//width:
            neighbours.append(neigh)
        neigh = i-1
        if neigh//width == i//width:
            neighbours.append(neigh)
        
        for neigh in neighbours:
            q[i].addConnectedNode(q[neigh])

    start = -1
    for i in range(len(data)):
        if data[i] == '0':
            if start == -1:
                start = i
            stop = i
            
    print(start, stop)
    dijkstra(q, start, stop)
    

    
def dijkstra(q, start_node, stop_node):
    s = []
    d = {i: float("inf") for i in q}
    d[start_node] = 0 
    p = {i: -1 for i in q}
    # while q:




class Node():
    def __init__(self, value, weight, connected_nodes):
        self.value = value
        self.weight = weight
        self.connected_nodes = connected_nodes

    def addConnectedNode(self, node):
        self.connected_nodes.append(node)

if __name__ == "__main__":
    #  main(sys.argv[1:])
    main()


        

