from flask import Blueprint
from .utils import *

db_blueprint = Blueprint('db', __name__)


@db_blueprint.get('/dbs')
def get_dbs():
    c = client()
    dbs = c.list_database_names()

    return dict(dbs=dbs)


@db_blueprint.get('/collections')
def get_collections():
    db = getdb()
    collections = db.list_collection_names()
    return dict(collections=collections)
