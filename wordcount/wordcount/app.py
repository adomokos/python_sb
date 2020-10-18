from flask import Flask
from os import environ as env
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


def run():
    app.run(host='0.0.0.0', port=env.get('PORT', 4000))
