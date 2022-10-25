from dao.model.film import Film


class FilmDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Film).all()

    def get_one(self, fid):
        return self.session.query(Film).get(fid)

    def get_by_director(self, did):
        return self.session.query(Film).filter(Film.director_id == did).all()

    def get_by_genre(self, gid):
        return self.session.query(Film).filter(Film.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Film).filter(Film.year == year).all()

    def post(self, film: Film):
        self.session.add(film)
        self.session.commit()
        return 'film added', 201

    def delete(self, fid):
        film = self.get_one(fid)
        self.session.delete(film)
        self.session.commit()
        return 'film deleted', 204

    def update(self, film: Film):
        self.session.add(film)
        self.session.commit()
        return 'film updated', 204




