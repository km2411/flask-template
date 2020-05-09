from flask import Blueprint, render_template, request, jsonify
import requests

from app.src.helpers import validations, config

# Define the blueprint:
math = Blueprint('math', __name__)
precompute_service_url = config.PRECOMPUTE_SERVICE

# Set the route and accepted methods
@math.route('/')
def index():
    return "This is an example app"


@math.route('/home')
def home():
    return render_template("home.html")


@math.route("/fib", methods=["POST"])
def fib_n():
    n = request.form["fib_n"]
    if not validations.validate_int(n):
        # in case of invalid input, return HTTP response code for Bad Request
        return "Please enter a valid input!", 400
    
    # call service 2
    fib_url = precompute_service_url + '/fib' 
    response = requests.post(url=fib_url, json={'fib_n':str(n)})
    return jsonify(response.text)


def ack_mn():
    return ""


def fact_n():
    return ""
