# create a class "WeightedGraph" which does the following
# Creates a graph with vertices and edges
# Creates an adjacency list with each vertex
# Records down the edge with the weight inside the adjacency list of the vertex
# Able to create undirected edges with the vertices inside the graph
from queue import PriorityQueue 
import math
from map.station import Station, build_adjacency_dict, get_station_name_by_code, get_codes_by_station_name, get_line

if __name__ == "__main__":
    adj_dict = build_adjacency_dict()
    print("Neighbours of BAYSHORE:", adj_dict["TE29"])
    print(get_station_name_by_code("DT32"))  # input: any station code / Output: station name
    print(get_codes_by_station_name("expo"))  # User input: any station name / Output: station code
    
def MRT_travel_algo(source: str, end: str): # source will be the station code
    distance = {}
    routing = {}
    # maybe change to distance dictionary ----> distance = {"DT1": (time), .....}
    for subclasses in Station.__subclasses__():
        for member in subclasses:
            distance[member.name] = math.inf # creates a dictionary with ALL the station code with inf dist at the start

    for subclasses in Station.__subclasses__():
        for member in subclasses:
            routing[member.name] = ""
            
    visited_edge = []
    distance[source] = 0 

    placeholder = PriorityQueue() # for python, you need to enter the comparator at the front of the tuple, i.e (priority, value)  -----> stations value are stored in (dst, time)
    # format for the items in the Heapq will be time, source, destination
    placeholder.put((0, source, source))

    while placeholder.qsize() != 0: # loop until the queue is gone
        currentEdge = placeholder.get() # when you poll, the edge is in the format (time,source,destination)  ----> first
        # for each of the edge, get the weight and find if the weight to the destination is lower than found
        destination = currentEdge[2] # extract the third element, the destination
        src = currentEdge[1]
        if distance[destination] > (distance[src] + currentEdge[0]):
            distance[destination] = (distance[src] + currentEdge[0]) # record new dis
            routing[destination] = routing[src] + src
        
        for values in adj_dict[destination]: # access the tuples which are in the format of dest, time
            if (values[1], destination, values[0]) not in visited_edge:
                visited_edge.append((values[1], destination, values[0]))
                placeholder.put((values[1], destination, values[0]))
    print(routing[end])
    return(distance[end])
    
print(MRT_travel_algo("DT32", "EW33"))



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