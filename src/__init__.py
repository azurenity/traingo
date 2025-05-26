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
    
    for subclasses in Station.__subclasses__():
        for member in subclasses:
            distance[member.name] = math.inf 
            routing[member.name] = []      
            
    visited_nodes = set()
    distance[source] = 0 
    placeholder = PriorityQueue()
    placeholder.put((0, source))  # format will be (current cost to arrive at the station, station)

    while not placeholder.empty(): 
        time, src = placeholder.get() # when you poll, the edge is in the format (time,source,destination)  ----> first
        if src in visited_nodes: # skips the src stations that has a current cost higher than the first occurance (i.e least) 
            continue
        visited_nodes.add(src)
        
        for values in adj_dict[src]:
            if (time + values[1]) < distance[values[0]]:
                distance[values[0]] = (time + values[1])
                routing[values[0]] = routing[src] + [src]
                placeholder.put((time + values[1], values[0]))

        
    route = ' --> '.join(routing[end] + [end])  # so now, it returns the pathing in station codes
        
    return(f'Time to reach the station is {distance[end]} minutes and the route to take is {route}')
    
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