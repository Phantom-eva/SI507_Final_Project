# UMICH SI 507 Final Project
### Summary

In this project, I am going to build a movie recommendation system. 

The system has two functions: 

1. Check out the latest movies and theaters where you can watch them
2. Give movie recommendation list and watch link according to filtering conditions

### Required Python packages

Install

```python
pip install google-search-results
```

Import

```python
import numpy as np
import json
import requests
import webbrowser
from flask import Flask 
from copy import deepcopy
from serpapi import GoogleSearch
```

### API Keys

Please create a file api_secrets.py and edit:

```python
TMDB_API_KEY = "your TMDB api key"
OMDB_API_KEY = "your OMDB api key"
GOOGLE_SEARCH_API_KEY = "your SERPAPI api key"
```

In order to obtain these api keys, please go to the website:

```python
https://www.themoviedb.org/documentation/api
https://www.omdbapi.com/
https://serpapi.com/showtimes-results
```

To use your keys:

```python
from api_secrets import TMDB_API_KEY, OMDB_API_KEY, GOOGLE_SEARCH_API_KEY
```

### Data Structure

Question tree:

<img src="F:\UMICH\2022 Fall\SI 507\final_pro\4.png" style="zoom:60%;" />

Movie data:

<img src="F:\UMICH\2022 Fall\SI 507\final_pro\2.png" style="zoom:67%;" />

### Interaction

```bash
python main.py
```

First, choose from two functions:

```bash
python ./main.py
-------------------------------------------------------------------------------------------

          #           #               # # #         #           #      #      # # # # #
         # #         # #            #       #        #         #       #      #
        #   #       #   #         #           #       #       #        #      #
       #     #     #     #       #             #       #     #         #      # # # # #
      #       #   #       #       #           #         #   #          #      #
     #         # #         #        #       #            # #           #      #
    #           #           #         # # #               #            #      # # # # #

-------------------------------------------------------------------------------------------

Hello, welcome to the movie recommendation system!
Hey, what do you want to do this time?
1: Go to the theater to watch the latest movie.
2: Search online for movies you want to watch.
Please choose 1 or 2: 
```

(1) Go to the theater to watch the latest movie:

```bash
Please choose 1 or 2: 1
Regarding the latest movies information, do you want to load it from the cache? Please enter yes or no: no
1: Black Adam
2: The Woman King
3: Avatar: The Way of Water
......
Please choose the number of a movie you want to watch: 4
Please enter your location (example: Ann Arbor, Michigan): Ann Arbor, Michigan
https://serpapi.com/search
Today
1: Cinemark Ann Arbor 20 and IMAX
4.9 mi
4100 Carpenter Road, Ypsilanti, MI 48197
['11:20 pm']
2: Emagine Canton
16.3 mi
39535 Ford Road, Canton, MI 48187
['10:45 pm']
Which theater do you want to see here for more information?
Please enter a number: 1
```

(2) Search online for movies you want to watch:

```bash
Please choose 1 or 2: 2
Regarding all movies information, do you want to load it from the cache? Please enter yes or no: yes
Please enter file name: all_movie_cache.json
----------use cache-----------
Get action movie data done!
Get adventure movie data done!
Get horror movie data done!
Get sci-fi movie data done!
Get comedy movie data done!
Get other movie data done!
Process action movie data done!
Process adventure movie data done!
Process horror movie data done!
Process sci-fi movie data done!
Process comedy movie data done!
Process other movie data done!
Do you want to watch an action movie? no
Do you want to watch an adventure movie? yes
Do you want to watch a movie longer than 120 minutes? yes
Do you want to watch a movie released after 2015? yes
1: Enola Holmes 2
2: Dune
3: Ghostbusters: Afterlife
4: Jumanji: The Next Level
......
This is the result.
Do you want to sort the movies based on popularity?
Please enter yes or no: yes
1: Enola Holmes 2
2: Dune
3: Ghostbusters: Afterlife
4: Aladdin
5: Jumanji: The Next Level
......
This is the sorted result.
Do you want to check more information of a specified movie?
Please enter yes or no: yes
Please enter a number between 1-10: 1
Title: Enola Holmes 2
Director: Harry Bradbeer
Actor: Millie Bobby Brown, Henry Cavill, David Thewlis
Runtime: 129
Rated: PG-13
Do you want to view in browser?
Please enter yes or no: yes
Launching https://www.themoviedb.org/movie/829280-enola-holmes-2/watch?locale=US in web browser...
```

