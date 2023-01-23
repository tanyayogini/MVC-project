from app.setup_db import db
from marshmallow import Schema, fields


# Модель жанра и схема сериализации
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreScheme(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
