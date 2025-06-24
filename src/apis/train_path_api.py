from flask import Blueprint, jsonify, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # adding the traingo file as a pythonpath in sys.path - fixes the import problems
from src.station_name_path import MRT_travel_algo 

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
    src = str(request.args.get('from')).upper()
    dst = str(request.args.get('to')).upper()
    
    ## LOGIC
    path = MRT_travel_algo(src, dst)
    return jsonify(status="OK", message=f'{path} !')

# You could add more routes related to 'status' in this file, for example:
# @status_bp.route("/status/details", methods=['GET'])
# def api_status_details():
#     return jsonify(status="OK", details="Some detailed status...")
