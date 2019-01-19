from flask import Blueprint
from flask_restplus import Resource, Api

API_BP = Blueprint('api', __name__)
API = Api(API_BP)

# The imported packages are placed here because they inherit from api
from .auth import *