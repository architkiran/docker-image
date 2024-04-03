from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return 'Hello this is archit trying to push a docker image'
