from flask import Blueprint, Response, g, render_template, request

from app.src.helpers import validations
from app.src.models.compute import Compute


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
    return str(Compute.fibonacci(int(n)))


def ack_mn():
    return ""


def fact_n():
    return ""
