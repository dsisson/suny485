from flask import Flask, request, jsonify
from suny485.projects.hw15.password_utils import evaluate_strength

app = Flask(__name__)


"""
To run this Flask app, at the command line, while in the folder for this homework
assignment run the following:
>>> python api.py

This API has two endpoints:
1. /get_strength, which accepts a GET request with a query string
2. /get_strength, which accepts a POST request with a JSON payload

To call the API with a GET request, make an http request like the following in your browser:
http://127.0.0.1:5000/get_strength?password=example

The browser will show you the following response:
{
  "password": "example",
  "strength": "bad"
}

For the purposes of our testing, we use the requests package to make HTTP requests. 
You can do live exploratory testing using ipython.

The commands for a GET request look like this:
# Set up the query params:
>>> params = {'password': 'example'}
>>> res = requests.get('http://127.0.0.1:5000/get_strength' params=params)
>>> res
<Response [200]>
>>> res.json()
{'password': 'example', 'strength': 'bad'}

To call the API with a POST request, make an HTTP request like the following:
# Set up the JSON payload:
>>> payload = {'password': 'example'}
>>> res = requests.post('http://127.0.0.1:5000/get_strength' json=payload)
>>> res
<Response [200]>
>>> res.json()
{'password': 'example', 'strength': 'bad'}

"""


@app.route('/get_strength', methods=['GET'])
def get_password_strength_by_get():
    """
        For the supplied password, with a valid GET request
        that includes a key `password` that has a str value
        return either 'good' or 'bad', depending on the results
        of the evaluate_strength method for the password.

        Expected request format:
        /get_strength?password=some_string

        Json structure to be returned::
        {
            'password': 'some string',
            'strength': 'good'/'bad'
        }
    """
    # Get the 'password' parameter from the query string
    password = request.args.get('password', '')
    strength = evaluate_strength(password)

    # build the response json payload
    response_data = {
        "password": password,
        "strength": 'good' if strength else 'bad'
    }

    return jsonify(response_data)


@app.route('/get_strength', methods=['POST'])
def get_password_strength_by_post():
    """
        For the supplied password, with a valid JSON POST payload
        that contains the key `password` with a string value, return
        either 'good' or 'bad', depending on the results of the
        evaluate_strength method for the password.

        Expected json payload format:
        {"password": "some_string"}

        Json structure to be returned::
        {
            'password': 'some string',
            'strength': 'good'/'bad'
        }
    """
    # Retrieve the JSON data from the request
    data = request.get_json()

    # Check if the JSON payload contains the expected keys
    if 'password' not in data:
        return jsonify({"error": "Missing key 'password' in the JSON payload"}), 400

    # Extract values from the json
    password = data['password']
    strength = evaluate_strength(password)

    # build the response json payload
    response_data = {
        "password": password,
        "strength": 'good' if strength else 'bad'
    }

    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(debug=True)
