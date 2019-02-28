""" Import everything from the blueprints """
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import CONFIG

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'


def create_app(config_name):
    """ Initialize Flask app
        : configure all neccessary environments
        : plus blueprints
    """
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(CONFIG[config_name])
    
    db.init_app(app)
    login_manager.init_app(app)

    from .api_1_0 import API_BP as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1')

    return app
