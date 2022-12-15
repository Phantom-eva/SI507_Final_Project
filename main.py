import json
import requests
import webbrowser
import numpy as np
from flask import Flask, render_template, request
from wsgiserver import WSGIServer
from serpapi import GoogleSearch

from api_secrets import GOOGLE_SEARCH_API_KEY, TMDB_API_KEY, OMDB_API_KEY
from tree import simplePlay, playLeaf, isLeaf, yes, treeNode, constrct_question_tree
from local_movie import getNewestMovie, getShowtimes
from cache import openCache, saveCache


Genre_list = {}


class Movie():
    ''' details of a movie

    Instance Attributes
    -------------------
    title: string
        the title of the movie
    adult: boolean
        whether the movie is adult rated
    genres: array(int)
        the genres of the movie
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    def __init__(self, title = "no title", adult = False, genres = "no genre", tmdb_id = 0, imdb_id = "no imdb id", language = "no language", director = "no director", actor = "no actor", release_date = "no release date", runtime = 0,  rating = "no rating", popularity = 0.00, url = "no url", json = None):
        self.title = title
        self.adult = adult
        self.genres = genres
        self.tmdb_id = tmdb_id
        self.imdb_id = imdb_id
        self.language = language
        self.director = director
        self.actor = actor
        self.release_date = release_date
        self.runtime = runtime
        self.rating = rating
        self.url = url
        self.popularity = popularity
        if json != None:
            self.title = json["title"]
            self.adult = json["adult"]
            self.genres = json["genre_ids"]
            self.tmdb_id = json["id"]
            self.language = json["original_language"]
            self.release_date = json["release_date"]
            self.popularity = json["popularity"]


def getLocalMovieData():
    ans_cache = input("Regarding the latest movie information, do you want to load it from the cache? Please enter yes or no: ")
    while (ans_cache != "yes" and ans_cache != "no"):
        ans_cache = input("Invalid input. Please enter yes or no: ")
    if ans_cache == "yes":
        file_name = input("Please enter the file name:")
        file_location = "./static/" + file_name
        newest_movie = openCache(file = file_location)
    else:
        newest_movie = getNewestMovie()
    newest_movie_list = []
    i = 1
    for item in newest_movie:
        newest_movie_list.append(Movie(json = item))
        print(str(i)+": "+item["title"])
        i += 1
    return newest_movie, newest_movie_list


def showLocalMovieData(newest_movie, newest_movie_list):
    number = input("Please choose the number of a movie you want to watch: ")
    while(not number.isdigit() or int(number) <= 0 or int(number) > len(newest_movie_list)):
        number = input("Invalid input. Please choose the number of a movie you want to watch: ")
    location = input("Please enter your location (example: Ann Arbor, Michigan): ")
    showtimes = getShowtimes(movie=newest_movie_list[int(number)-1].title, location=location)
    theater_num = 1
    print(showtimes[0]["day"])
    for theater in showtimes[0]["theaters"]:
        print(str(theater_num) + ": " + theater["name"])
        print(theater["distance"])
        print(theater["address"])
        print(theater["showing"][0]["time"])
        theater_num += 1
    print("Which theater do you want to see here for more information?")
    ans_browser = input("Please enter a number: ")
    while(not ans_browser.isdigit() or int(ans_browser)<=0 or int(ans_browser)>theater_num-1):
        ans_browser = input("Invalid input. Please enter a valid number: ")
    print("Launching " + showtimes[0]["theaters"][int(ans_browser)-1]["link"] + " in web browser...")
    webbrowser.open(showtimes[0]["theaters"][int(ans_browser)-1]["link"])
    print("Do you want to save the latest movie information to the cache?")
    ans_cache = input("Please enter yes or no: ")
    while (ans_cache != "yes" and ans_cache != "no"):
        ans_cache = input("Invalid input. Please enter yes or no: ")
    if ans_cache == "yes":
        file_name = input("Please enter file name: ")
        file_location = "./static/" + file_name
        saveCache(file=file_location,cache_dict = newest_movie)
    print("Do you want to run this system again or exit?")
    ans_next = input("Please enter again or exit: ")
    while(ans_next != "again" and ans_next != "exit"):
        ans_next = input("Invalid input. Please enter again or exit: ")
    if ans_next == "again":
        play()
    else:
        exit()


def getAllMovieData():
    action_movie_list = get_genre_movie("action")
    q_1 = constrct_question_tree()
    simplePlay(q_1)


def showAllMoviedata():
    pass


def get_genre_movie(genre):
    ''' details of a movie

    '''
    base_url = "https://api.themoviedb.org/3/discover/movie"
    data = []
    movie_list = []
    for page in range(25):
        para = {
            "api_key": TMDB_API_KEY,
            "with_genre": genre,
            "page": page + 1
        }
        r = requests.get(url=base_url, params=para)
        data.extend(r.json()['results'])
    for item in data:
        movie_list.append(Movie(json=item))
    return movie_list


def process_data(data):
    ''' details of a movie

    '''
    movie_list = []
    return movie_list



def sort_movie_list(movie_list):
    ''' details of a movie

    Instance Attributes
    -------------------

    '''
    pass


def play():
    ''' run the movie recommendation system once
    '''
    print("Hey, what do you want to do this time? ")
    print("1: Go to the theater to watch the latest movie.")
    print("2: Search online for movies you want to watch.")
    ans_type = input("Please choose 1 or 2: ")
    while(ans_type != "1" and ans_type != "2"):
        ans_type = input("Invalid input. Please enter 1 or 2: ")
    if ans_type == "1":
        newest_movie, newest_movie_list = getLocalMovieData()
        showLocalMovieData(newest_movie=newest_movie, newest_movie_list=newest_movie_list)
    elif ans_type == "2":
        getAllMovieData()
        showLocalMovieData()


def main():
    print("-------------------------------------------------------------------------------------------")
    print("                                                                                           ")
    print("          #           #               # # #         #           #      #      # # # # #    ")
    print("         # #         # #            #       #        #         #       #      #            ")
    print("        #   #       #   #         #           #       #       #        #      #            ")
    print("       #     #     #     #       #             #       #     #         #      # # # # #    ")
    print("      #       #   #       #       #           #         #   #          #      #            ")
    print("     #         # #         #        #       #            # #           #      #            ")
    print("    #           #           #         # # #               #            #      # # # # #    ")
    print("                                                                                           ")
    print("-------------------------------------------------------------------------------------------")
    print("                                                                                           ")
    print("Hello, welcome to the movie recommendation system!")
    play()  


# flask part
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