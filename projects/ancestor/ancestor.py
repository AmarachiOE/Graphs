from graph import Graph
from util import Stack, Queue 

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # first create vertices of the parents/ancestors for graph (1st elem of each pair)
    
    for i in range (0, len(ancestors)):
        vertex = ancestors[i][0]
        graph.add_vertex(vertex)

    # then create edges to the children for each parent/ancestor/vertex (2nd elem of each pair)
    # can't use add_edge() bc of condition

    for i in range (0, len(ancestors)):
        vertex = ancestors[i][0]
        edge = ancestors[i][1]
        graph.vertices[vertex].add(edge) 

    # print the vertex dictionary    
    print("Vertices: ", graph.vertices)
    

    # FIRST CHECK: 
    # if starting_node does not have parents (is not a value in the dictionary)
    # return -1
    # so first need to get all the values in dictionary
    values = []
    for key in graph.vertices:
        for value in graph.vertices[key]:
            values.append(value)
    
    print("All Values: ", values)
    
    if starting_node not in values:
        return -1

    # now search through edges to find the starting_node. If the starting_node is found as an edge for multiple keys, pick the lowest key and set that as earliest_ancestor. Now look to see if that key is an edge for another (lowest) key... keep going until the key found is not an edge for another key and return the earliest_ancestor

    q = Queue()
    q.enqueue(starting_node)

    earliest_ancestor = starting_node
    

    while q.size():
        parents = []
        child = q.dequeue()
        print("Current child: ", child)

        

        for key in graph.vertices:
            if child in graph.vertices[key]:
                parents.append(key)
        
        print("Parents: ", parents)
        
        if len(parents) == 0:
            return child

        else: 
            lowest_parent = min(parents)
            earliest_ancestor = lowest_parent
            q.enqueue(lowest_parent)

            


    # if starting_node in list(graph.vertices.values()):
    #     earliest_ancestor = True

    return earliest_ancestor, parents, starting_node

def findLowestParent(someGraph, value):

    parents = []
    # lowest_parent = min(parents)

    for key in someGraph.vertices:
        if value in someGraph.vertices[key]:
            parents.append(key)

    lowest_parent = min(parents)

    return lowest_parent





test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 7))


# self notes:
# print("Values: ", list(graph.vertices.values()))

# wanted to use .add_edge(vertex, edge) but there's a condition in graph.py that both the vertex and the edge need to be in graph.vertices before an edge can be successfully added. however some edges are solely children and vertices are only those nodes that have children
# graph.add_edge(vertex, edge)