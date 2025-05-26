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
        
        for values in adj_dict[src]: # goes through the node's adjacency list to find out the distance between its neighbours
            if (time + values[1]) < distance[values[0]]:
                distance[values[0]] = (time + values[1])
                routing[values[0]] = routing[src] + [src]
                placeholder.put((time + values[1], values[0]))

        
    route = ' --> '.join(routing[end] + [end])  # so now, it returns the pathing in station codes
        
    return(f'Time to reach the station is {distance[end]} minutes and the route to take is {route}')
    
print(MRT_travel_algo("DT32", "EW33"))



"""
NEXT STEPS: 

1. Output the route more nicely
2. Consider using a database (SQL) for further learning
3. Output potential train wait timings as they are not factored into the equation
a) Consider peak and non peak timings
4. Fix the LRT timings and also add in both LRT stations
5. Way to take in a user input

"""