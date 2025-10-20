from .error_codes import invalid_station_code, invalid_station_name
from .station import MRT_stations

def get_station_name_by_code(code):
    """
    Return the station name corresponding to a given station code.
    If not found, returns None.
    """
    if code in MRT_stations:
        station = MRT_stations.get(code)
        return station.name
    return invalid_station_code


def get_codes_by_station_name(name):
    """
    Return a comma-separated string of codes corresponding to a given station name.
    If not found, returns None.
    """
    temp = []
    for stations_code in MRT_stations:
        station = MRT_stations[stations_code]
        if station.name.lower() == name.lower():
            temp.append(stations_code)
                
    if temp == []:
        return invalid_station_name
    else:
        return ', '.join(temp)
     
def get_line(name):
    codes = get_codes_by_station_name(name) 
    if codes == invalid_station_name:
        return invalid_station_name
    
    
    new = codes.split(", ")
    for i in range(len(new)):
        new[i] = new[i][:2] + "L"
        
    return f"{name} belongs to the following lines: {', '.join(new)}" 

def build_adjacency_dict():
    """
    Build an adjacency dictionary for all MRT stations.

    Returns:
        dict[str, list[tuple[str, int]]]: A dictionary where each key is a
        station code and the value is a list of (destination_code, travel_time) pairs.
    """
    graph = {}
    for code, station in MRT_stations.items(): # iterates thru the stations in the subclasses     
        graph.setdefault(code, set()) # adds an empty set if it is not inside the dict 
        for travel in station.travel: # accesses the travel info of the stations
            dst, t = travel.destination, travel.time # takes the destination, time
            graph[code].add((dst, t))
            graph.setdefault(dst, set())  # adds the an empty set when its not inside the dict for the dst
            graph[dst].add((code, t)) # Add reverse neighbor for dst
                
    for code in MRT_stations: 
        graph[code] = list(graph[code]) # converts the elements in the graph back into lists for better accessibility for the algo
    return graph

## Process the input given
def is_Valid(src, dst): # checks the src and the dst given
    lst = [get_station_name_by_code(src), get_codes_by_station_name(src), get_station_name_by_code(dst), get_codes_by_station_name(dst)]
    for i in range(len(lst)):
        if lst[i] == invalid_station_code or lst[i] == invalid_station_name:
            lst[i] = False
        else:
            lst[i] = True
    if not lst[0] and not lst[1]:
        return False
    elif not lst[2] and not lst[3]:
        return False
    else:
        return True
    
def convert_stations(src, dst):
    lst = [get_station_name_by_code(src), get_codes_by_station_name(src), get_station_name_by_code(dst), get_codes_by_station_name(dst)]
    if not lst[0] == invalid_station_code: # meaning there is station code
        lst[0] = get_station_name_by_code(src)
        lst[1] = src
    else:
        lst[0] = src
        if "," in get_codes_by_station_name(src):
            temp = get_codes_by_station_name(src).split(',')
            lst[1] = temp[0] # meaning is that there is no line specified
        else:
            lst[1] = get_codes_by_station_name(src)
    
    if not lst[2] == invalid_station_code:
        lst[2] = get_station_name_by_code(dst)
        lst[3] = dst
    else:
        lst[2] = dst
        if "," in get_codes_by_station_name(dst):
            temp = get_codes_by_station_name(dst).split(',')
            lst[3] = temp[0]
        else:
            lst[3] = get_codes_by_station_name(dst)    
    
    return lst

"""
def name_dict():
    graph = {}
    for subclasses in Station.__subclasses__():  # iterates thru the subclasses
        for member in subclasses: # iterates thru the stations in the subclasses
            name = get_station_name_by_code(member.name)     
            graph.setdefault(name, set()) # adds an empty set if it is not inside the dict
            for travel in member.value.travel: # accesses the travel info of the stations
                dst, t = get_station_name_by_code(travel.destination), travel.time # takes the destination, time
                if dst == name:
                    continue
                graph[name].add((dst, t)) 
                graph.setdefault(dst, set())  # adds the an empty set when its not inside the dict for the dst
                graph[dst].add((name, t)) # Add reverse neighbor for dst
                
    for subclasses in Station.__subclasses__():  # iterates thru the subclasses
        for member in subclasses: 
            graph[name] = list(graph[name]) # converts the elements in the graph back into lists for better accessibility for the algo
    return graph
    
"""