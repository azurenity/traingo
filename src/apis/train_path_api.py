from flask import Blueprint, jsonify, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # adding the traingo file as a pythonpath in sys.path - fixes the import problems
from src.station_code_path import MRT_travel_algo
from src.map.station import is_Valid, convert_stations
from src.map.error_codes import invalid_input

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
    
    if not is_Valid(src, dst):
        return jsonify(message = invalid_input)

    ## LOGIC
    
    lst = convert_stations(src, dst) # into format of name, code, name, code
    if lst[1] == lst[3]:
        return jsonify(message='It will take 0 minutes as its the same station') # AVOIDS CASES WHERE INTERCHANGES BREAKS THE CODE
    
    time = MRT_travel_algo(lst[1], lst[3])
    return jsonify(message=f'{time}')