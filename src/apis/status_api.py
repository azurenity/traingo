from flask import Blueprint, jsonify

# Create a Blueprint for status-related APIs
# The first argument is the Blueprint's name, often matching the module name.
# The second argument, __name__, helps Flask locate templates/static files if you add them later.
# url_prefix will prepend '/api/v1' to all routes defined in this blueprint.
status_bp = Blueprint('status_api', __name__, url_prefix='/api/v1')

@status_bp.route("/status", methods=['GET'])
def api_status():
    """A simple API endpoint to check the status.
       This route will be accessible at /api/v1/status due to the url_prefix.
    """
    return jsonify(status="OK", message="Traingo API is running from status_api blueprint!")

# You could add more routes related to 'status' in this file, for example:
# @status_bp.route("/status/details", methods=['GET'])
# def api_status_details():
#     return jsonify(status="OK", details="Some detailed status...")
