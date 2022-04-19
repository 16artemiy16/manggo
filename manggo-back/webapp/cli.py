import logging
import click

log = logging.getLogger(__name__)


def register(app):
    @app.cli.command('list-routes')
    def list_routes():
        for url in app.url_map.iter_rules():
            click.echo(f'{url.rule} {url.methods} {url.endpoint}')
