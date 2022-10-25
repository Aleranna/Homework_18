from flask import request

from dao.film import FilmDAO
from dao.model.film import Film


class FilmService:

    def __init__(self, dao: FilmDAO):
        self.dao = dao

    def get_one(self, fid):
        return self.dao.get_one(fid)

    def get_by_director(self, director):
        return self.dao.get_by_director(director)

    def get_by_genre(self, genre):
        return self.dao.get_by_genre(genre)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def post(self, data):
        film = Film(**data)
        return self.dao.post(film)

    def update(self, fid, data):
        film = self.dao.get_one(fid)

        film.title = data.get('title')
        film.description = data.get('description')
        film.trailer = data.get('trailer')
        film.year = data.get('year')
        film.rating = data.get('rating')
        film.genre_id = data.get('genre_id')
        film.director_id = data.get('director_id')

        return self.dao.update(film)

    def delete(self, fid):
        return self.dao.delete(fid)

    def get_by_filter(self, director, genre, year):
        if director is not None:
            return self.dao.get_by_director(director)
        elif genre is not None:
            return self.dao.get_by_genre(genre)
        elif year is not None:
            return self.dao.get_by_year(year)
        else:
            return self.dao.get_all()

