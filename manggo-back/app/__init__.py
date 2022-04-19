from flask import Flask


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    from .main.controllers import main_blueprint

    app.register_blueprint(main_blueprint)

    return app
