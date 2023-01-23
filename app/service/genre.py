from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)
