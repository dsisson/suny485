from flask import Flask, request, jsonify
from suny485.projects.hw14.password_utils import evaluate_strength

app = Flask(__name__)


"""
To run this Flask app, at the command line, while in the folder for this homework
assignment run the following:
>>> python api.py

To call the API, make an http request like the following:
>>> http://127.0.0.1:5000/get_strength?password=example

This api will return a json payload like the following:
{'password': 'example', 'strength': 'bad'}

To see this json, you will have to actually get the json. The commands look like this:
>>> res = requests.get(f"{url}/get_strength?password=example")
>>> res
<Response [200]>
>>> res.json()
{'password': 'example', 'strength': 'bad'}

"""


@app.route('/get_strength', methods=['GET'])
def get_password_strength():
    """
        For the supplied password, return either 'good' or 'bad',
        depending on the results of the evaluate_strength method for
        the password.

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


if __name__ == '__main__':
    app.run(debug=True)
