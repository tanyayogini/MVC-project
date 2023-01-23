from app.setup_db import db
from marshmallow import Schema, fields


# Модель режиссера и схема сериализации
class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DirectorScheme(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
