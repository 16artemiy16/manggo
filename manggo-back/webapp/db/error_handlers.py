import logging
from pymongo.errors import ServerSelectionTimeoutError


def register(blueprint):
    @blueprint.errorhandler(ServerSelectionTimeoutError)
    def handle_mongo_timeout(e):
        logging.debug(f'Failed connect to MongoDB by timeout, {e._message}')

        return dict(
            success=False,
            msg='Failed connecting mongo for the given time. Check the connection string or try increase the timeout.',
        ), 408
