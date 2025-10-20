from flask import Blueprint, jsonify, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # adding the traingo file as a pythonpath in sys.path - fixes the import problems
from src.map.station import get_station_name_by_code
from src.map.error_codes import invalid_station_code


name_bp = Blueprint('get_station_name_api', __name__, url_prefix='/api/v1')

@name_bp.route("/name", methods=['GET'])
def api_lines():
    """A simple API endpoint to output the path taken from source to destination and the timing.
       This route will be accessible at /api/v1/path due to the url_prefix.
    """
    ## paramURL, query params
    station_code = str(request.args.get('code'))
    line = station_code[0:2] + "L"
    ## LOGIC
    station_name = get_station_name_by_code(station_code)
    print(station_name)
    if station_name == invalid_station_code:
        return jsonify(message = f'{station_name}')
        
    return jsonify(message=f'Station name is: {station_name} {line} MRT Station')
