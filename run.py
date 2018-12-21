from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource

APP = Flask(__name__)

APP.config.from_object(os.environ['APP_SETTINGS'])
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)

# it is placed here because it's classes inherit from DB
# Makes the table available for runing migrations

from app.auth.models import User


# makes the endpoint available for consumption
from app import *


if __name__ == '__main__':
    APP.run()
