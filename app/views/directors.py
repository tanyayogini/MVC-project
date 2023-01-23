from flask_restx import Namespace, Resource

from app.dao.model.director import DirectorScheme
from implemented import director_service

director_ns = Namespace('directors')
director_scheme = DirectorScheme()
directors_scheme = DirectorScheme(many=True)


# Представления для получения всех режиссеров и режиссера по Id
@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_scheme.dump(directors), 200


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_scheme.dump(director), 200
