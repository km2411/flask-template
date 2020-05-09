# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Initialzie Database
from app.src.helpers.database import mongo
from app.src.helpers.config import DBURI
mongo.init_app(app, uri=DBURI) 

# Import a module / component using its blueprint handler variable
from app.src.views.math_functions import math 

# Register blueprint(s)
app.register_blueprint(math)
