from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data):
        add_movie = Movie(**data)
        self.session.add(add_movie)
        self.session.commit()
        return add_movie

    def update(self, updated_movie):
        self.session.add(updated_movie)
        self.session.commit()

    def delete(self, deleted_movie):
        self.session.delete(deleted_movie)
        self.session.commit()
