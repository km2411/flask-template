from flask import Blueprint, Response, g, render_template, request

from app.module_one.src.models.compute import Compute
from app.module_one.src.helpers import validations

# Define the blueprint: 'home', set its url prefix: app.url/home
mod_home = Blueprint('home', __name__, url_prefix='/home')
mod_math = Blueprint('math', __name__, url_prefix='/fib')

# Set the route and accepted methods
@mod_home.route('/home')
def home():
    return render_template("app/module_one/src/templates/home.html")


@mod_math.route("/fib", methods=["POST"])
def fib_n():
    n = request.form["fib_n"]
    if not validations.validate_int(n):
        return "Please enter a valid input!", 400
    return str(Compute.fibonacci(int(n)))


@mod_math.route("/ack", methods=["POST"])
def ack_mn():
    return ""


@mod_math.route("/fact", methods=["POST"])
def fact_n():
    return ""
    