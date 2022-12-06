import numpy as np
import json
import requests
from flask import Flask, render_template, request
from wsgiserver import WSGIServer
from serpapi import GoogleSearch
from api_secrets import GOOGLE_SEARCH_API, TMDB_API_KEY, OMDB_API_KEY
from cache import open_cache, save_cache
from tree import simplePlay, playLeaf, isLeaf, yes


CACHE_FILENAME = "./cache/movie_cache.json"
GENRES = ["Action", "Adventure", "Comedy", "Crime", "Drama", "Mystery", "Romance", "Science Fiction", "Thriller", "War"]


Action_list = []

my_cache = {}


class Movie():
    def __init__(self, title = "no title", genres = "no genre", imdb_id = "no imdb id", language = "no language", release_date = "no release date", runtime = "no time", rated = "Not rated", director = "no director", actor = "no actor", average_rating = "no rating", url = "no url", json = None):
        self.title = title
        self.genres = genres
        self.imdb_id = imdb_id
        self.language = language
        self.director = director
        self.actor = actor
        self.release_date = release_date
        self.runtime = runtime
        self.rated = rated
        self.average_rating = average_rating
        self.url = url
        if json != None:
            self.title = title
            self.genres = genres
            self.imdb_id = imdb_id
            self.language = language
            self.director = director
            self.actor = actor
            self.release_date = release_date
            self.runtime = runtime
            self.rated = rated
            self.url = url


def search_by_keywords(keywords):

def get_data():
    base_url = "https://api.themoviedb.org/3/movie/76341"
    para = {
        "with_genre": "Action"
    }
    r = requests.get(url=base_url,params=para)
    data = r.json()
    return data


def process_data(data):
    movie_list = []
    return movie_list


def get_local_cinema_data(location):
    params = {
        "q": "eternals theater",
        "location": location,
        "hl": "en",
        "gl": "us",
        "api_key": GOOGLE_SEARCH_API
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    showtimes = results["showtimes"]

def sort_movie_list(movie_list):
    pass


def play():
    ans_1 = input("Do you want to search for movies that are playing at local cinemas or something else? Please enter local or else: ")
    while(ans_1 != "local" and ans_1 != "else"):
        ans_1 = input("Invalid input. Please enter local or else: ")
    if ans_1 == "local":
        location = input("Please enter your location (example: Ann Arbor, MI, USA): ")
        get_local_cinema_data(location)
    else:
        ans_2 = input("Do you want to search by keywords? Please enter yes or no: ")
        while(ans_2 != "yes" and ans_2 != "no"):
            ans_2 = input("Invalid input. Please enter yes or no: ")
        if ans_2 == "yes":
            keywords = input("Please enter the keywords: ")
            res_keywords = 
def main():
    print("Hello, welcome to the movie recommendation system!")
    play()
    
    




# using flask, under construction

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/search_by_keywords")
# def s_keywords():
#     return render_template("search_by_keywords.html")

# @app.route("/search_by_filter")
# def s_filter():
#     return render_template("search_by_filter.html")

# @app.route("/search_local_theater")
# def s_local():
#     return render_template("search_local_theater.html")


if __name__ == '__main__':
    # print('starting Flask app', app.name)
    # # Debug/Develpment mode
    # app.run(debug=True)

    # # Production mode
    # http_server = WSGIServer(('', 5000),app)
    # http_server.serve_forever()

    main()