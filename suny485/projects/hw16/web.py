from flask import Flask, render_template, request
from flask_htmx import HTMX
import requests

web = Flask(__name__)
htmx = HTMX()
htmx.init_app(web)


"""
To run this Flask app, at the command line, while in the folder for this homework
assignment run the following:
>>> python web.py

This will launch a server on your local host, which will be either
"http://localhost" or "http://127.0.0.1". The port will be 8080. This must
NOT be the same port that the API runs on.

This web has one page:
1. "/" (i.e., http://127.0.0.1:8080), which loads a form

This web app also has a path that accepts http POSTs, but that is not connected
to any web page. You will get an error if you try to access it directly in your browser.
"""

# this is the host + port for the API app, when it's running
api_host = 'http://127.0.0.1:5000'


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/lookup_password', methods=['POST'])
def lookup_password():
    password = request.form.get('password', '')

    # make the http POST against the API
    response = requests.post(f"{api_host}/get_strength", json={'password': password})

    return response.text


if __name__ == '__main__':
    web.run(port=8080, debug=True)
