from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
from os import environ as env

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import Result

@app.route('/')
def hello():
    return "Hello World!"


def run():
    app.run(host='0.0.0.0', port=env.get('PORT', 4000))


if __name__ == '__main__':
    run()
