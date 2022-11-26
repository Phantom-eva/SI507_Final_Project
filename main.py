import numpy as np
import json
import requests
from flask import Flask, render_template, request
from wsgiserver import WSGIServer

CACHE_FILENAME = "./cache/movie_cache.json"
TMDB_API_KEY = "1e84af3a40a9581586adbbce0d8390a1"
OMDB_API_KEY = "48b724a0"
GENRES = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "TV Movie", "Thriller", "War", "Western"]

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

 
class Question():
    pass

def open_cache():
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict):
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)
    fw.close() 

def get_data():
    base_url = "https://api.themoviedb.org/3/movie/76341"

def process_data():
    pass

def main():
    pass

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return render_template("templates/index.html")

@app.route("/")
def hello() -> str:
    return "Hello World"


if __name__ == '__main__':
    print('starting Flask app', app.name)
    # Debug/Develpment mode
    # update_static_images()
    # app.run(debug=True)

    # # Production mode
    # http_server = WSGIServer(('', 5000),app)
    # http_server.serve_forever()