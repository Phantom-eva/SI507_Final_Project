'''
This file is used to get a list of movies in theatres and showtimes of these movies.
'''
import requests
from serpapi import GoogleSearch
from api_secrets import GOOGLE_SEARCH_API_KEY, TMDB_API_KEY


def getShowtimes(movie,location):
    params = {
        "q": movie,
        "location": location,
        "hl": "en",
        "gl": "us",
        "api_key": GOOGLE_SEARCH_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    showtimes = results["showtimes"]
    return showtimes

def getNewestMovie():
    base_url = "https://api.themoviedb.org/3/movie/now_playing"
    params = {
        "api_key": TMDB_API_KEY
    }
    r = requests.get(url=base_url, params=params)
    newest_movie_list = r.json()['results']
    return newest_movie_list