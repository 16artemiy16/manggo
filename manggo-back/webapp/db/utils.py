from flask import request
from pymongo import MongoClient


def client():
    host = request.args.get('host', None)
    port = request.args.get('port', None, int)

    return MongoClient(host, port)


def getdb():
    dbname = request.args.get('dbname', None)
    c = client()
    return c.get_database(dbname)
