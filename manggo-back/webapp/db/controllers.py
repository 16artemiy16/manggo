from flask import Blueprint
from . import utils
from . import error_handlers

db_blueprint = Blueprint('db', __name__)

error_handlers.register(db_blueprint)


@db_blueprint.get('/dbs')
def get_dbs():
    c = utils.client()
    dbs = c.list_database_names()

    return dict(dbs=dbs)


@db_blueprint.get('/collections')
def get_collections():
    db = utils.getdb()
    collections = db.list_collection_names()
    return dict(collections=collections)
