import requests
import webbrowser
from api_secrets import TMDB_API_KEY, OMDB_API_KEY
from tree import simplePlay, loadQuestionTree
from local_movie import getNewestMovie, getShowtimes
from cache import openCache, saveCache
from copy import deepcopy


class Movie():
    ''' 
    details of a movie

    Instance Attributes
    -------------------
    title: string
        the title of the movie
    rated: string
        whether the movie is for adult or for others
    genres: array(int)
        the genres of the movie
    tmdb_id: int
        the id for the movie in TMDB database
    imdb_id: string or null
        the id for the movie in IMDB database
    language: string
        the language mainly used in the movie
    director: string
        the director of the movie
    actor: string
        the actor of the movie
    release_date: string (format: date)
        the release_date of the movie
    runtime: int or null
        the runtime of the movie
    rating: int
        the rating score of the movie
    popularity: number
        whether the movie is popular
    url: string
        the link to check more information
    '''
    def __init__(self, title = "no title", rated = "no rated", genres = "no genre", tmdb_id = 0, imdb_id = "no imdb id", language = "no language", director = "no director", actor = "no actor", release_date = "0000-00-00", runtime = 0,  rating = "no rating", popularity = 0.00, url = "no url", json = None):
        try:
            self.title = json["title"]
        except:
            self.title = title
        try:
            self.rated = json["rated"]
        except:
            self.rated = rated
        try:
            self.genres = json["genre_ids"]
        except:
            self.genres = genres
        try:
            self.tmdb_id = json["id"]
        except:
            self.tmdb_id = tmdb_id
        try:
            self.imdb_id = json["imdb_id"]
        except:
            self.imdb_id = imdb_id
        try:
            self.language = json["original_language"]
        except:
            self.language = language
        try:
            self.director = json["director"]
        except:
            self.director = director
        try:
            self.actor = json["actor"]
        except:
            self.actor = actor
        try:
            self.release_date = json["release_date"]
            if self.release_date == "":
                self.release_date = release_date
        except:
            self.release_date = release_date
        try:
            self.runtime = json["runtime"]
        except:
            self.runtime = runtime
        try:
            self.rating = json["rating"]
        except:
            self.rating = rating
        try:
            self.popularity = json["popularity"]
        except:
            self.popularity = popularity
        try:
            self.url = json["url"]
        except:
            self.url = url
        
        

def getLocalMovieData():
    '''
    get movie in theater list

    Return
    ---------------------------
    newest_movie: list
        used for cache
    newest_movie_list: list
        object list
    '''
    ans_cache = input("Regarding the latest movies information, do you want to load it from the cache? Please enter yes or no: ")
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
    '''
    show options: 
    1. choose which movie do you want to watch
    2. choose which theater do you want to go
    3. choose whether you want to view in browser
    '''
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
        end()


def getAllMovieData():
    '''
    get all movie data from OMDB and TMDB
    '''
    ans_cache = input("Regarding all movies information, do you want to load it from the cache? Please enter yes or no: ")
    while(ans_cache != "yes" and ans_cache != "no"):
        ans_cache = input("Invalid input. Please enter yes or no: ")
    if ans_cache == "yes":
        file_name = input("Please enter file name: ")
        file_location = "./static/" + file_name
        Movie_List = openCache(file=file_location)
        print("----------use cache-----------")
        All_Movie_Data = {}
        Movie_List["action"], All_Movie_Data["action"] = getGenreMovie(data=Movie_List["action"],genre="28")
        print("Get action movie data done!")
        Movie_List["adventure"], All_Movie_Data["adventure"] = getGenreMovie(data=Movie_List["adventure"],genre="12",without_genre="28")
        print("Get adventure movie data done!")
        Movie_List["horror"], All_Movie_Data["horror"] = getGenreMovie(data=Movie_List["horror"],genre="27",without_genre="28,12")
        print("Get horror movie data done!")
        Movie_List["sci-fi"], All_Movie_Data["sci-fi"] = getGenreMovie(data=Movie_List["sci-fi"],genre="878",without_genre="28,12,27")
        print("Get sci-fi movie data done!")
        Movie_List["comedy"], All_Movie_Data["comedy"] = getGenreMovie(data=Movie_List["comedy"],genre="35",without_genre="28,12,27,878")
        print("Get comedy movie data done!")
        Movie_List["other"], All_Movie_Data["other"] = getGenreMovie(data=Movie_List["other"],without_genre="28,12,27,878,35")
        print("Get other movie data done!")
        All_Movie_Data_processed = processData(All_Movie_Data)
    else:
        All_Movie_Data = {}
        Movie_List = {}
        Movie_List["action"], All_Movie_Data["action"] = getGenreMovie(genre="28")
        print("Get action movie data done!")
        Movie_List["adventure"], All_Movie_Data["adventure"] = getGenreMovie(genre="12", without_genre="28")
        print("Get adventure movie data done!")
        Movie_List["horror"], All_Movie_Data["horror"] = getGenreMovie(genre="27", without_genre="28,12")
        print("Get horror movie data done!")
        Movie_List["sci-fi"], All_Movie_Data["sci-fi"] = getGenreMovie(genre="878", without_genre="28,12,27")
        print("Get sci-fi movie data done!")
        Movie_List["comedy"], All_Movie_Data["comedy"] = getGenreMovie(genre="35", without_genre="28,12,27,878")
        print("Get comedy movie data done!")
        Movie_List["other"], All_Movie_Data["other"] = getGenreMovie(without_genre="28,12,27,878,35")
        print("Get other movie data done!")
        All_Movie_Data_processed = processData(All_Movie_Data)
    return Movie_List, All_Movie_Data_processed


def showAllMovieData(movie_list,movie_list_processed):
    '''
    show options: 
        ask filter questions, give results, and sort
    filter question:
        Do you want to watch an action movie?
        Do you want to watch an adventure movie?
        Do you want to watch an horror movie?
        Do you want to watch an sci-fi movie?
        Do you want to watch an comedy movie?
        Do you want to watch a movie longer than 120 minutes?
        Do you want to watch a movie released after 2015?
    '''
    tree = loadQuestionTree()
    filter = simplePlay(tree)
    result_list = movie_list_processed[filter[0]][filter[1]]
    for i in range(min(10,len(result_list))):
        print(str(i+1) + ": " + result_list[i].title)
    print("This is the result.")
    print("Do you want to sort the movies based on popularity?")
    ans_sort = input("Please enter yes or no: ")
    while(ans_sort != "yes" and ans_sort != "no"):
        ans_sort = input("Invalid input. Please enter yes or no: ")
    if ans_sort == "yes":
        result_list = sortMovieList(result_list)
        for i in range(min(10,len(result_list))):
            print(str(i+1) + ": " + result_list[i].title)
        print("This is the sorted result.")
    print("Do you want to check more information of a specified movie?")    
    ans_check = input("Please enter yes or no: ")
    while(ans_check != "yes" and ans_check != "no"):
        ans_check = input("Invalid input. Please enter yes or no: ")
    if ans_check == "yes":
        num_check = input("Please enter a number between 1-10: ")
        while(not num_check.isdigit() or int(num_check)<=0 or int(num_check)>10):
            num_check = input("Invalid input. Please enter a number between 1-10: ")
        print("Title: " + result_list[int(num_check)-1].title)
        print("Director: " + result_list[int(num_check)-1].director)
        print("Actor: " + result_list[int(num_check)-1].actor)
        print("Runtime: " + str(result_list[int(num_check)-1].runtime))
        print("Rated: " + result_list[int(num_check)-1].rated)
        print("Do you want to view in browser? ")
        ans_brow = input("Please enter yes or no: ")
        while(ans_brow != "yes" and ans_brow != "no"):
            ans_brow = input("Invalid input. Please enter yes or no: ")
        if ans_brow == "yes":
            print("Launching " + result_list[int(num_check)-1].url + " in web browser...")
            webbrowser.open(result_list[int(num_check)-1].url) 
    print("Do you want to save the latest all movie information to the cache?")
    ans_cache = input("Please enter yes or no: ")
    while (ans_cache != "yes" and ans_cache != "no"):
        ans_cache = input("Invalid input. Please enter yes or no: ")
    if ans_cache == "yes":
        file_name = input("Please enter file name: ")
        file_location = "./static/" + file_name
        saveCache(file=file_location,cache_dict = movie_list)
    print("Do you want to run this system again or exit?")
    ans_next = input("Please enter again or exit: ")
    while(ans_next != "again" and ans_next != "exit"):
        ans_next = input("Invalid input. Please enter again or exit: ")
    if ans_next == "again":
        play()
    else:
        end()


def getGenreMovie(data = None, genre=None, without_genre=None):
    ''' 
    get movie list based on given genre

    Return
    -----------------------------
    data: list
        used for cache
    movie_list: list
        object list
    '''
    if data == None:
        if without_genre == None and genre != None:
            base_url = "https://api.themoviedb.org/3/discover/movie"
            data = []
            for page in range(50):
                para = {
                    "api_key": TMDB_API_KEY,
                    "with_genres": genre,
                    "page": page + 1
                }
                r = requests.get(url=base_url, params=para)
                data.extend(r.json()['results'])
        elif without_genre != None and genre == None:
            base_url = "https://api.themoviedb.org/3/discover/movie"
            data = []
            for page in range(50):
                para = {
                    "api_key": TMDB_API_KEY,
                    "without_genres": without_genre,
                    "page": page + 1
                }
                r = requests.get(url=base_url, params=para)
                data.extend(r.json()['results'])
        else:
            base_url = "https://api.themoviedb.org/3/discover/movie"
            data = []
            for page in range(50):
                para = {
                    "api_key": TMDB_API_KEY,
                    "with_genres": genre,
                    "without_genres": without_genre,
                    "page": page + 1
                }
                r = requests.get(url=base_url, params=para)
                data.extend(r.json()['results'])
        for item in data:
            # movie_item = Movie(json=item)
            url_detail_tmdb = "https://api.themoviedb.org/3/movie/" + str(item["id"])
            para_detail_tmdb = {
                "api_key": TMDB_API_KEY,
                "language": "en-US"
            }
            r_detail_tmdb = requests.get(url=url_detail_tmdb,params=para_detail_tmdb)
            data_detail_tmdb = r_detail_tmdb.json()
            url_detail_tmdb_2 = "https://api.themoviedb.org/3/movie/" + str(item["id"]) + "/watch/providers"
            para_detail_tmdb_2 = {
                "api_key": TMDB_API_KEY,
            }
            r_detail_tmdb_2 = requests.get(url=url_detail_tmdb_2,params=para_detail_tmdb_2)
            data_detail_tmdb_2 = r_detail_tmdb_2.json()["results"]
            url_detail_omdb = "http://www.omdbapi.com/"
            para_detail_omdb = {
                "apikey": OMDB_API_KEY,
                "i": data_detail_tmdb["imdb_id"]
            }
            r_detail_omdb = requests.get(url=url_detail_omdb,params=para_detail_omdb)
            data_detail_omdb = r_detail_omdb.json()

            item["imdb_id"] = data_detail_tmdb["imdb_id"]
            item["runtime"] = data_detail_tmdb["runtime"]
            try:
                item["url"] = data_detail_tmdb_2["US"]["link"]
            except:
                item["url"] = "no url"
            try:
                item["director"] = data_detail_omdb["Director"]
            except:
                item["director"] = "no director"
            try:
                item["actor"] = data_detail_omdb["Actors"]
            except:
                item["actor"] = "no actor"
            try:
                item["rated"] = data_detail_omdb["Rated"]
            except:
                item["rated"] = "no rated"
            try:
                item["rating"] = data_detail_omdb["Ratings"]
            except:
                item["rating"] = "no rating"
    else:
        data = data
    movie_list = []
    for item in data:
        movie_list.append(Movie(json=item))
    return data, movie_list


def processData(movie_list):
    ''' 
    process movie data based on filter conditions

    '''
    movie_list["action"] = selectData(movie_list["action"])
    print("Process action movie data done!")
    movie_list["adventure"] = selectData(movie_list["adventure"])
    print("Process adventure movie data done!")
    movie_list["horror"] = selectData(movie_list["horror"])
    print("Process horror movie data done!")
    movie_list["sci-fi"] = selectData(movie_list["sci-fi"])
    print("Process sci-fi movie data done!")
    movie_list["comedy"] = selectData(movie_list["comedy"])
    print("Process comedy movie data done!")
    movie_list["other"] = selectData(movie_list["other"])
    print("Process other movie data done!")
    return movie_list


def selectData(movie_list):
    '''
    select movie data based on filter conditions
    '''
    return_list = {}
    return_list["long_new"] = []
    return_list["long_old"] = []
    return_list["short_new"] = []
    return_list["short_old"] = []
    for item in movie_list:
        if item.runtime > 120 and int(item.release_date[0:4])>=2015:
            return_list["long_new"].append(item)
        elif item.runtime > 120 and int(item.release_date[0:4])<2015:
            return_list["long_old"].append(item)
        elif item.runtime <= 120 and int(item.release_date[0:4])>=2015:
            return_list["short_new"].append(item)
        elif item.runtime <= 120 and int(item.release_date[0:4])<2015:
            return_list["short_old"].append(item)
    return return_list


def sortMovieList(movie_list):
    ''' 
    sort movie list based on popularity
    '''
    return_list = deepcopy(movie_list)
    return_list.sort(key=lambda x: x.popularity, reverse=True)
    return return_list


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
        movie_list,movie_list_processed = getAllMovieData()
        showAllMovieData(movie_list,movie_list_processed)


def end():
    print("Good Bye!")
    exit()


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