from flask import request
from flask_restx import Namespace, Resource

from app.dao.model.movie import MovieScheme
from implemented import movie_service

movies_ns = Namespace('movies')
movie_scheme = MovieScheme()
movies_scheme = MovieScheme(many=True)


# Представления для фильмов: получение всех фильмов, фильмов по фильтрам, добавление нового фильма
@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        data = {
            'director_id': request.args.get('director_id'),
            'genre_id': request.args.get('genre_id'),
            'year': request.args.get('year')
        }
        movies = movie_service.get_by_parameters(data)
        return movies_scheme.dump(movies), 200

    def post(self):
        data = request.json
        add_movie = movie_service.create(data)
        return '', 201, {'location': f'movies/{add_movie.id}'}


# Представления для получения фильма по Id, обновления фильма, удаления фильма
@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_scheme.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_service.update(data)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
