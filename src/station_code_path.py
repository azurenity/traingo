from queue import PriorityQueue 
import math
from src.map.station import MRT_stations
from src.map.functions import build_adjacency_dict

adj_dict = build_adjacency_dict()

def MRT_travel_algo(source: str, end: str): # source and end are station codes
    distance = {}
    routing = {}
    
    for code in MRT_stations:
        distance[code] = math.inf 
        routing[code] = []      
            
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

    route = ' --> '.join(routing[end] + [end])
      
    return(f'Time to reach the station including transfer timing is {distance[end]} minutes and path taken is {route}')

""" if you want to only return the stations that are of focus (interchanges)
# Next job is to change the way the route is outputted. 
# 1. to check the routing list (by accessing the dict) and then outputting only when the lines change
# a) can be done by checking the first two letters in the list then changing when it detects a change
# b) save the station where it switches lines

    temp = routing[end] # takes the list from the dictionary
    path = [temp[0]]
    line = temp[0][:1]
    for i in range(1, len(temp)):
        if line not in temp[i]:
            line = temp[i][:1]
            path.append(temp[i]) # change line and add the station
"""
