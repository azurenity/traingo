from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Traingo Flask App!"

@app.route("/api/v1/status", methods=['GET'])
def api_status():
    """A simple API endpoint to check the status."""
    return jsonify(status="OK", message="Traingo API is running!")

# You can add more API endpoints here, for example:
# from .apis import some_api_blueprint # If you structure APIs in blueprints
# app.register_blueprint(some_api_blueprint, url_prefix='/api/v1/some_feature')

def main():
    """This function can be used if you want to run any setup before starting Flask.
       For simple cases, just app.run() is enough.
    """
    print("Starting Flask development server...")
    # Host '0.0.0.0' makes the server accessible from your network, not just localhost.
    # Use a different port if 5000 is taken.
    # debug=True is for development; REMOVE or set to False for production.
    app.run(host='127.0.0.1', port=5000, debug=True)

if __name__ == "__main__":
    main()
