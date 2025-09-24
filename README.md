# Traingo

This is a project that assists in commuter's daily travel by calculating the best route and time needed for the commuter to travel within Singapore's MRT network.

## Usage of Traingo

### User Experience

The User will be able to input their initial location and the location that they want to go to.
They will then be given the shortest path they can take and the corresponding travel time.

## Development

### Using UV

This application uses `uv` as a package manager.
First, install [`uv`](https://github.com/astral-sh/uv) on your device.

#### Getting Environment Ready

To allow the code to run, we will need to first sync up the dependencies using this command:
```
uv sync
```

#### Adding a Package

When we want to add a package:
```
uv add <package>
```

## Running the Application

To start the Flask development server:

### On Linux/macOS:

1.  Ensure the script is executable (only needs to be done once):
    ```bash
    chmod +x traingo.sh
    ```
2.  Run the script:
    ```bash
    ./traingo.sh
    ```

### On Windows:

Run the batch script:
```batch
traingo.bat
```

The application will be available at `http://127.0.0.1:5000` by default.

## Running Tests

This project uses `pytest` for running unit tests. Ensure `pytest` and project dependencies are installed (refer to the `uv sync` command above).

To run the tests:

### On Linux/macOS:

1.  Make the test script executable (only needs to be done once):
    ```bash
    chmod +x run_tests.sh
    ```
2.  Run the script:
    ```bash
    ./run_tests.sh
    ```

### On Windows:

Run the batch script:
```batch
run_tests.bat
```

### To initialise the App (on Postman):

Start the main.py in src. This will initialise the Flask server in the ip address mentioned. Afterwards you can interact with the api to output the travel data required.