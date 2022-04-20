from flask import request
from pymongo import MongoClient
from . import constants


def client():
    host = request.args.get('host', None)
    port = request.args.get('port', None, int)
    timeout = request.args.get('timeout', constants.DEFAULT_MONGO_TIMEOUT_MS, int)

    return MongoClient(host, port, serverSelectionTimeoutMS=timeout)


def getdb():
    dbname = request.args.get('dbname', None)
    c = client()
    return c.get_database(dbname)
