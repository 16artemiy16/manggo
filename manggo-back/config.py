import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    LOGGER = dict(
        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler("dev.log"),
            logging.StreamHandler()
        ]
    )
