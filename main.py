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


class treeNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)


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


# construct question tree
def constrct_question_tree():
    node_1 = treeNode("Do you want to watch an action movie?") 
    node_2 = treeNode("Do you want to watch an adventure movie?") 
    node_3 = treeNode("Do you want to watch an comedy movie?") 
    node_4 = treeNode("Do you want to watch an crime movie?") 
    node_5 = treeNode("Do you want to watch an drama movie?") 
    node_6 = treeNode("Do you want to watch an mystery movie?")
    node_7 = treeNode("Do you want to watch an romance movie?") 
    node_8 = treeNode("Do you want to watch an science fiction movie?") 
    node_9 = treeNode("Do you want to watch an thriller movie?")
    node_10 = treeNode("Do you want to watch an war movie?")
    node_1.right = node_2
    node_2.right = node_3
    node_3.right = node_4
    node_4.right = node_5
    node_5.right = node_6
    node_6.right = node_7
    node_7.right = node_8
    node_8.right = node_9
    node_9.right = node_10


def main():
    pass

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_by_keywords")
def s_keywords():
    return render_template("search_by_keywords.html")

@app.route("/search_by_filter")
def s_filter():
    return render_template("search_by_filter.html")

@app.route("/search_local_theater")
def s_local():
    return render_template("search_local_theater.html")


if __name__ == '__main__':
    print('starting Flask app', app.name)
    # # Debug/Develpment mode
    app.run(debug=True)

    # # Production mode
    # http_server = WSGIServer(('', 5000),app)
    # http_server.serve_forever()