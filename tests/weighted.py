# create a class "WeightedGraph" which does the following
# Creates a graph with vertices and edges
# Creates an adjacency list with each vertex
# Records down the edge with the weight inside the adjacency list of the vertex
# Able to create undirected edges with the vertices inside the graph
import heapq

class WeightedGraph():

    def __init__(self, vertices):
        self.vertices = vertices       
        self.adjacency_list = [[] for _ in range(vertices)]  # creates a empty list for each vertex

    def addUndirectedEdge(self, source, destination, weight):
        front = [source, destination, weight] # Adds the edge in one direction
        self.adjacency_list[source].append(front)

    def addUndirectedEdge(self, source, destination, weight):
        front = [source, destination, weight]
        back = [destination, source, weight]

        self.adjacency_list[source].append(front)
        self.adjacency_list[destination].append(back)

    def getVertices(self):
        return self.adjacency_list
    
    def Dijkstra_Algo(WeightedGraph, Vertex):
        distance = [inf] * len(g.getVertices())

        placeholder = []
        heapq.heapify(placeholder)
        

    
g = WeightedGraph(5)
g.addUndirectedEdge(1,4,6)
g.addUndirectedEdge(2,4,3)
g.addUndirectedEdge(1,3,2)
print(g.getVertices()) 


# can add deletion of edges as well if possible
# edit such that it can be done with stations


# To create the Algo, you require the algo to do the following:

"""
1. Take in a WeightedGraph and its starting vertex
2. Create a distance from the starting vertex to all vertices and start it with all values being infinity (as large as possible)
3. Add a dummy edge from the starting vertex to itself, causing it to have a weight of 0 to the heapq in order to start the algo
4. Continue with a While loop where the following occurs:
a) poll the heapq to pop the edge with the edge with the least weight
b) Continue to the next point:
bi) if the next point is not visited, update with the new distance
bii) if the next point has been visited, if the new distance is shorter than the previously found, update the list
c) add the edges of the destination to the heapq
d) run the loop until the heapq is empty
"""


        


