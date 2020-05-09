from flask import Blueprint, Response, g, render_template, request, jsonify
from app.src.helpers.database import mongo
from app.src.models.compute import Compute

# Define the blueprint:
fetch_result = Blueprint('fetch_result', __name__)


@fetch_result.route("/precomputed/fib", methods=["POST"])
def fib_n():
    # First check if result present already in database
    n = request.args.get('fib_n')
    result = mongo.db.fibonacci.find_one({"n": n})
    response = {}
    if result:
        response[str(n)] = str(result['value'])    
        return jsonify(response)
    # If result not present, compute the result and also store in database for future
    value = str(Compute.fibonacci(int(n)))
    mongo.db.fibonacci.insert_one({'n': n, 'value': value})
    response[str(n)] = value
    return jsonify(response)


def ack_mn():
    return ""


def fact_n():
    return ""
