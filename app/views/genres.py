from flask_restx import Namespace, Resource

from app.dao.model.genre import GenreScheme
from implemented import genre_service

genre_ns = Namespace('genres')
genre_scheme = GenreScheme()
genres_scheme = GenreScheme(many=True)


# Представления для получения всех жанров и одного жанра по id
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_scheme.dump(genres), 200


@genre_ns.route('/<int:gid>/')
class GenresView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_scheme.dump(genre), 200
