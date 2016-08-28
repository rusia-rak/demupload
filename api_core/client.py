import json
# from api_core.models import Movie, Genre
from requests.auth import HTTPBasicAuth
import requests
from time import sleep

# endpoint = 'https://evening-refuge-8247.herokuapp.com/api/movies/'
movie_endpoint = 'https://evening-refuge-8247.herokuapp.com/api/movies/'
genre_endpoint = 'https://evening-refuge-8247.herokuapp.com/api/genres/'
input_file = open("../imdb.json")
movies_list = json.load(input_file)

genre_list = []

for movie in movies_list:
	genre_list += movie['genre']

genre_list = [genre.lstrip() for genre in genre_list]
genre_list = list(set(genre_list))
for genre in genre_list:
	data = {'genre_name':genre}
	resp = requests.post(genre_endpoint, data, auth=HTTPBasicAuth('kushan','pass'))
	print resp.json()

for movie in movies_list:
	print data
	data = {'name':movie['name'],
		'director':movie['director'],
		'imdb_score':movie['imdb_score'],
		'popularity_99':movie['99popularity'],
		'genre':[genre.lstrip() for genre in movie['genre']]
	}
	resp = requests.post(movie_endpoint, data, auth=HTTPBasicAuth('kushan','pass'))
	print resp

# for id in range(249, 253):
# 	internal_endpoint = endpoint + str(id)
# 	resp = requests.delete(internal_endpoint, auth=HTTPBasicAuth('kushan','pass'))
# 	print resp
# if __name__ == '__main__':
# 	main()