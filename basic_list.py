import requests
from api_secrets import TMDB_API_KEY

def get_genre_list():
    base_genre_url = "https://api.themoviedb.org/3/genre/movie/list"
    para_genre = {
        "api_key": TMDB_API_KEY,
        "language": "en-us"
    }
    r = requests.get(url = base_genre_url, params = para_genre)
    genre_list = r.json()["genres"]
    return genre_list


def get_certif_list():
    base_certif_url = "https://api.themoviedb.org/3/certification/movie/list"
    para_certif = {
        "api_key": TMDB_API_KEY
    }
    r = requests.get(url = base_certif_url, params = para_certif)
    genre_list = r.json()["certifications"]["US"]
    return genre_list

