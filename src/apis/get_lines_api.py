from flask import Blueprint, jsonify, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # adding the traingo file as a pythonpath in sys.path - fixes the import problems
from src.map.station import get_line


lines_bp = Blueprint('get_lines_api', __name__, url_prefix='/api/v1')

@lines_bp.route("/lines", methods=['GET'])
def api_lines():
    """A simple API endpoint to output the path taken from source to destination and the timing.
       This route will be accessible at /api/v1/path due to the url_prefix.
    """
    ## paramURL, query params
    stn = str(request.args.get('station'))
        
    ## LOGIC
    lines = get_line(stn)
    print(lines)
    return jsonify(message=f'Station has the following lines: {lines}')


# problem as theres too many apis and the program will only execute one