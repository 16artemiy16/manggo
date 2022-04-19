from flask import Blueprint

main_blueprint = Blueprint(
    'main',
    __name__,
)


@main_blueprint.get('/')
def ping():
    return 'Hello from Manggo!'
