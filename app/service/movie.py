from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_by_parameters(self, data):
        # Фильтрация фильмов: если был передан id режиссера, жанра или год, то возвращаются
        # соответствующие фильмы
        if data.get('director_id') is not None:
            return self.dao.get_by_director(data.get('director_id'))
        elif data.get('genre_id') is not None:
            return self.dao.get_by_genre(data.get('genre_id'))
        elif data.get('year') is not None:
            return self.dao.get_by_year(data.get('year'))
        else:
            return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        updated_movie = self.get_one(mid)
        # В задании не уточнено - полное обновление или частичное, поэтому учтем
        # случай, если для обновления переданы только частичные данные
        if data.get('title'):
            updated_movie.title = data.get('title')
        if data.get('description'):
            updated_movie.description = data.get('description')
        if data.get('trailer'):
            updated_movie.trailer = data.get('trailer')
        if data.get('year'):
            updated_movie.year = data.get('year')
        if data.get('rating'):
            updated_movie.rating = data.get('rating')
        if data.get('genre_id'):
            updated_movie.genre_id = data.get('genre_id')
        if data.get('director_id'):
            updated_movie.director_id = data.get('director_id')
        self.dao.update(updated_movie)

    def delete(self, mid):
        deleted_movie = self.get_one(mid)
        self.dao.delete(deleted_movie)
