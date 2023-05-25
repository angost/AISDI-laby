import argparse
import sys

def main(arguments):
# def main():
    filename = arguments[0]
    # filename = "graf2.txt"
    with open(filename, 'r') as filehandle:
        data = filehandle.read()
    data = data.split()
    width = len(data[0])
    height = len(data)
    data = "".join(data)

    q = []
    for i in range(len(data)):
        q.append(Node(i, int(data[i]), []))

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

    print("Start-node:", start, "Stop-node:", stop)
    dijkstra(q, q[start], q[stop])

def dijkstra(q, start_node, stop_node):
    s = []
    d = {i: float("inf") for i in q}
    d[start_node] = 0
    p = {i: -1 for i in q}
    while q:
        min_d = min(q, key = lambda node : d[node])
        q.remove(min_d)
        s.append(min_d)
        for neighbour in min_d.connected_nodes:
            if neighbour in q:
                # Jesli odleglosc sasieda od start-wierzcholka jest wieksza, to znaczy ze lepiej isc sciezka przez min_d stamtad do sasiada
                if d[neighbour] > d[min_d] + neighbour.weight:
                    d[neighbour] = d[min_d] + neighbour.weight
                    p[neighbour] = min_d


    print("\nShortest distance:", d[stop_node], "\n")
    found_p = 0
    current_node = stop_node
    print("Shortest path from stop_node to start_node: (index, weight)")
    print(stop_node.value, stop_node.weight)
    while True:
        found_p = p[current_node]
        current_node = found_p
        if found_p == -1:
            break
        print(found_p.value, found_p.weight)
    return d[stop_node]


class Node():
    def __init__(self, value, weight, connected_nodes):
        self.value = value
        self.weight = weight
        self.connected_nodes = connected_nodes

    def addConnectedNode(self, node):
        self.connected_nodes.append(node)

if __name__ == "__main__":
    main(sys.argv[1:])
    # main()




