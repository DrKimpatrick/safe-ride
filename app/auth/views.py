import os
from flask_restplus import Resource

class Environment(Resource):
    """ Class doc string """

    def get(self):
        """ Method doc string """
        return {'Environment': '{}'.format(os.environ['APP_SETTINGS'])}
