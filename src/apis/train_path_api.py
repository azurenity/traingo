from flask import Blueprint, jsonify, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # adding the traingo file as a pythonpath in sys.path - fixes the import problems
from src.station_code_path import MRT_travel_algo
from src.station_name_path import Name_travel_algo  
from src.map.station import get_station_name_by_code, get_codes_by_station_name

# Create a Blueprint for status-related APIs
# The first argument is the Blueprint's name, often matching the module name.
# The second argument, __name__, helps Flask locate templates/static files if you add them later.
# url_prefix will prepend '/api/v1' to all routes defined in this blueprint.
train_bp = Blueprint('train_path_api', __name__, url_prefix='/api/v1')

@train_bp.route("/path", methods=['GET'])
def api_status():
    """A simple API endpoint to output the path taken from source to destination and the timing.
       This route will be accessible at /api/v1/path due to the url_prefix.
    """
    ## paramURL, query params
    src = str(request.args.get('from'))
    dst = str(request.args.get('to'))
    
    if src == dst:
        return jsonify(message='It will take 0 minutes as its the same station')
    
    ## Process the input given
    lst = [get_station_name_by_code(src), get_codes_by_station_name(src), get_station_name_by_code(dst), get_codes_by_station_name(dst)]
    for i in range(len(lst)):
        if lst[i] == "Please give a correct Station code" or lst[i] == "Please give a correct Station name":
            lst[i] = False
        else:
            lst[i] = True
    print(lst)
    if not lst[0] and not lst[1]:
        return jsonify(message='Kindly input two valid station codes or station names')
    elif not lst[2] and not lst[3]:
        return jsonify(message='Kindly input two valid station codes or station names')
  
    if lst[0]: # meaning there is station code
        lst[0] = get_station_name_by_code(src)
        lst[1] = src
    else:
        lst[0] = src
        lst[1] = get_codes_by_station_name(src)
    
    if lst[2]:
        lst[2] = get_station_name_by_code(dst)
        lst[3] = dst
    else:
        lst[2] = dst
        lst[3] = get_codes_by_station_name(dst)
    
    print(lst)
    ## LOGIC
    
    # problems as of now > 
    # - if the input received is not the same name (CAPITALISATION) of the one in the database, the code bricks
    # - both inputs has to be either a station code or a station name, need a checker to see if they are the same type OR convert both to the same type

    

    time = MRT_travel_algo(lst[1], lst[3])
    return jsonify(message=f'{time}')

# You could add more routes related to 'status' in this file, for example:
# @status_bp.route("/status/details", methods=['GET'])
# def api_status_details():
#     return jsonify(status="OK", details="Some detailed status...")
