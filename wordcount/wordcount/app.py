from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ as env
import os
from .extensions import db
from .models import Result


def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    register_extensions(app)
    migrate = Migrate(app, db)
    return app


def register_extensions(app):
    db.init_app(app)


app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


def run():
    app.run(host='0.0.0.0', port=env.get('PORT', 4000))


if __name__ == '__main__':
    run()
