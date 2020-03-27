from flask import Flask
from flask_cors import CORS

from .extensions import db, ma
from .routes import category

def create_app(config_filename='config.py'):
    app = Flask(__name__)
    CORS(app)
    app.config.from_pyfile(config_filename)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(category)

    with app.app_context():
        db.create_all()

    return app

