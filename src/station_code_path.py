from queue import PriorityQueue 
import math
from src.map.station import Station, build_adjacency_dict, get_station_name_by_code, get_codes_by_station_name, get_line

adj_dict = build_adjacency_dict()

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

# problem arises when im going from lets say: EW1 to CC19. It goes to DT9 then calculates the timing to change to the CC19
# sol is to just create a secondary function that takes in the station name then outputs the timing