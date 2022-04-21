from flask import Flask
import logging


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    logging.basicConfig(**app.config.get('LOGGER', {}))

    from .main.controllers import main_blueprint
    from .db.controllers import db_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(db_blueprint)

    return app
