import requests
from api_secrets import TMDB_API_KEY
from cache import saveCache

def getGenreList():
    base_genre_url = "https://api.themoviedb.org/3/genre/movie/list"
    para_genre = {
        "api_key": TMDB_API_KEY,
        "language": "en-us"
    }
    r = requests.get(url = base_genre_url, params = para_genre)
    genre_list = r.json()["genres"]
    return genre_list


def getCertifList():
    base_certif_url = "https://api.themoviedb.org/3/certification/movie/list"
    para_certif = {
        "api_key": TMDB_API_KEY
    }
    r = requests.get(url = base_certif_url, params = para_certif)
    genre_list = r.json()["certifications"]["US"]
    return genre_list


def main():
    genre_list = getGenreList()
    file_genre_name = "genre_list.json"
    file_genre_location = "./static/" + file_genre_name
    certif_list = getCertifList()
    file_certif_name = "certif_list.json"
    file_certif_location = "./static/" + file_certif_name
    saveCache(file=file_genre_location,cache_dict=genre_list)
    saveCache(file=file_certif_location,cache_dict=certif_list)

if __name__ == "__main__":
    main()

