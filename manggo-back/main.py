from flask import Flask

app = Flask(__name__)


@app.get('')
def ping():
    return 'Hello from Manggo BACK'


if __name__ == '__main__':
    app.run()
