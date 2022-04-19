import os
from webapp import create_app
from webapp import cli

env = os.environ.get('APP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())

cli.register(app)

if __name__ == '__main__':
    app.run()
