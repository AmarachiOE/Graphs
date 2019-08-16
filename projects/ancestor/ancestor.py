from graph import Graph
from util import Stack, Queue 

# FIRST:
# Create function that takes in input and generates/populates a new Graph()
# Make sure the function returns the graph
# The input will be the ancestors list 

def createGraph(input): 
    graph = Graph()

    # First create vertices of the parents/ancestors for graph (1st elem of each pair)
    for i in range (0, len(input)):
        vertex = input[i][0]
        graph.add_vertex(vertex)

    # Second create edges to the children for each parent/ancestor/vertex (2nd elem of each pair)
    # Note: can't use add_edge() bc of condition
    for i in range (0, len(input)):
        vertex = input[i][0]
        edge = input[i][1]
        graph.vertices[vertex].add(edge) 

    # Print the vertex dictionary    
    print("Vertices: ", graph.vertices)

    return graph


def earliest_ancestor(ancestors, starting_node):

    # Invoke createGraph() function and pass in ancestors, save returned graph as graph
    graph = createGraph(ancestors)

    # EDGE CASE: 
    # If starting_node does not have parents, meaning it is not a value in the dictionary, return -1
    # So first need to get all the values in dictionary
    values = []
    for key in graph.vertices:
        for value in graph.vertices[key]:
            values.append(value)
    
    print("All Values: ", values)
    
    if starting_node not in values:
        return -1

    # Now create a Queue
    # Enqueue the starting_node
    # While queue has size/not empty...
        # Create empty parents array to populate
        # Retrieve the child we want to search for its parents by dequeueing the queue
        # Now we want to see if the child is a value in any of the keys in the graph
        # If child is among the values of a key,...
        # Append that key to parents array
        # Once all values have been searched/parents have been appended
        # If no parents were found (parent array is still empty)... 
        # Return that child as it is it's earliest ancestor
        # Else, if parent(s) were found...
        # Retrieve the lowest_parent (based off of ReadMe)
        # Enqueue the lowest_parent
        # While loop persists, this time the child is now the lowest_parent from the previous round
        # Will continue until no parents were found (parent array remained empty) and child is returned


    q = Queue()
    q.enqueue(starting_node)
    
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
            q.enqueue(lowest_parent)

    


#### TESTING

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 3))


# self notes:
# print("Values: ", list(graph.vertices.values()))

# wanted to use .add_edge(vertex, edge) but there's a condition in graph.py that both the vertex and the edge need to be in graph.vertices before an edge can be successfully added. however some edges are solely children and vertices are only those nodes that have children
# graph.add_edge(vertex, edge)