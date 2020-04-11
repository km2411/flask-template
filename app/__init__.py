# Import flask and template operators
from flask import Flask, render_template
# Define the WSGI application object
app = Flask(__name__)

# Import a module / component using its blueprint handler variable
from app.module_one.src.resources import math_resource

# Register blueprint(s)
app.register_blueprint(math_resource.mod_home)
app.register_blueprint(math_resource.mod_math)
