from flask import Flask

app = Flask(__name__)

from apis.status_api import status_bp
from apis.train_path_api import train_bp as bp1

app.register_blueprint(status_bp)
app.register_blueprint(bp1)

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
