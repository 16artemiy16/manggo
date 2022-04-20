from pymongo.errors import ServerSelectionTimeoutError


def register(blueprint):
    @blueprint.errorhandler(ServerSelectionTimeoutError)
    def handle_mongo_timeout(e):
        res = dict(
            success=False,
            msg='Failed connecting mongo for the given time. Check the connection string or try increase the timeout.',
        )

        return res, 408
