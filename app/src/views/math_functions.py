from flask import Blueprint, Response, g, render_template, request, jsonify

from app.src.helpers import validations
from app.src.models.compute import Compute
from app.src.helpers.database import mongo

# Define the blueprint:
math = Blueprint('math', __name__)


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

    # First check if result present already in database
    result = mongo.db.fibonacci.find_one({"n": n})
    if result:
        return result['value']    
    # If result not present, compute the result and also store in database for future
    response = {}
    value = str(Compute.fibonacci(int(n)))
    mongo.db.fibonacci.insert_one({'n': n, 'value': value})
    response[str(n)] = value
    return jsonify(response)


def ack_mn():
    return ""


def fact_n():
    return ""
