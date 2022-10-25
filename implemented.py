from dao.director import DirectorDAO
from dao.film import FilmDAO
from dao.genre import GenreDAO
from service.director import DirectorService
from service.film import FilmService
from service.genre import GenreService
from setup_db import db

film_dao = FilmDAO(db.session)
film_service = FilmService(film_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
