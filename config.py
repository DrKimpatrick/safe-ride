""" Configurations file """
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Parent configurations class """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '%q@vzm)&ag&ftcv+9a8tb55-hw@6*4dez#$%$1rxq57ddv@&9t'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """ Production configurations  """
    DEBUG = False


class StagingConfig(Config):
    """ Staging configurations """
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """ Development configurations """
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    """ Test configurations """
    TESTING = True

# Summarise the app configurations
CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
