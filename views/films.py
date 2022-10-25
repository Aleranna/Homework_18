from flask import request
from flask_restx import Resource, Namespace

from dao.model.film import FilmSchema
from implemented import film_service

film_ns = Namespace('films')
film_schema = FilmSchema()
films_schema = FilmSchema(many=True)


@film_ns.route('/')
class FilmsView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        films = film_service.get_by_filter(director_id, genre_id, year)
        return films_schema.dump(films)

    def post(self):
        data = request.json
        return film_service.post(data)


@film_ns.route('/<int:fid>')
class FilmView(Resource):
    def get(self, fid):
        film = film_service.get_one(fid)
        return film_schema.dump(film)

    def put(self, fid):
        data = request.json
        return film_service.update(fid, data)

    def delete(self, fid):
        return film_service.delete(fid)




