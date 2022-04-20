import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
