from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db

from app.views.movies import movies_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns


def create_app(config_object):
    """Принимает объект класса Config, возвращает приложение"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extension(app)
    return app


def register_extension(app):
    """Принимает приложение, инициализирует базу данных и регистрирует неймспейсы"""
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    with app.app_context():
        db.create_all()


app = create_app(Config())

if __name__ == '__main__':
    app.run()
