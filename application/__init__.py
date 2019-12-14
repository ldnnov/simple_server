from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        from . import routes, models

        db.init_app(app)
        db.create_all()

        # Create row for counter
        db.session.add(models.Counter())
        db.session.commit()

        return app
