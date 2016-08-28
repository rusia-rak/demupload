from rest_framework.test import APIClient
from django.test import TestCase
from api_core.models import Movie, Genre
import json
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

def add_genres():
    first_genre = Genre(genre_name='Adventure')
    second_genre = Genre(genre_name='Family')
    third_genre = Genre(genre_name='Fantasy')
    fourth_genre = Genre(genre_name='Musical')
    fifth_genre = Genre(genre_name='Action')
    sixth_genre = Genre(genre_name='Sci-Fi')
    first_genre.save()
    second_genre.save()
    third_genre.save()
    fourth_genre.save()
    fifth_genre.save()
    sixth_genre.save()
    return first_genre, second_genre, third_genre, fourth_genre, fifth_genre, sixth_genre

def add_movies():

    first_movie = Movie(name='The Wizard of Oz',\
        director='Victor Fleming', \
        imdb_score=8.3,\
        popularity_99=83.0)
    second_movie = Movie(name='Star Wars',\
        director='George Lucas',\
        imdb_score=8.8,\
        popularity_99=88.0)
    first_movie.save()
    second_movie.save()

    return first_movie, second_movie

class GenreTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(username='myname',\
            email='email@email.com', password='123456')
        self.client.login(username=self.admin.username, password='123456')

        self.first_genre, self.second_genre, self.third_genre, self.fourth_genre, \
        self.fifth_genre, self.sixth_genre = add_genres()

    def tearDown(self):
        self.client.logout()

    def test_http_get_retrieves_list_of_genres_and_returns_200(self):
        response = self.client.get('/api/genres/')
        genres = json.loads(response.content)
        self.assertEqual(response.status_code, 200)

    def test_http_get_will_return_json_object_for_each_genre(self):
        response = self.client.get('/api/genres/')
        self.assertEqual(len(response.data['results']), 6)

    def test_detail_genres_endpoint_returns_attributes_for_given_genre_id(self):
        response = self.client.get('/api/genres/{}/'.format(self.first_genre.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'genre_name': 'Adventure', 'id': 1})

    def test_http_post_will_create_genre_and_return_201(self):
        data = {'genre_name': 'History'}
        response = self.client.post('/api/genres/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['genre_name'], 'History')

    def test_http_post_without_data_returns_400(self):
        response = self.client.post('/api/genres/', {})
        self.assertEqual(response.status_code, 400)    
    
    def test_http_put_will_update_first_genre_and_return_200(self):
        data = {'genre_name': 'updated_name'}
        response = self.client.put('/api/genres/{}/'.format(self.second_genre.pk), data)
        self.assertEqual(response.status_code, 200)

    def test_http_put_will_update_first_genre_and_return_updated_genre_json(self):
        data = {'genre_name': 'updated_name'}
        response = self.client.put('/api/genres/{}/'.format(self.first_genre.pk), data)
        self.assertEqual(response.data['genre_name'], 'updated_name')

    def test_http_delete_will_remove_first_genre_and_return_204(self):
        response = self.client.delete('/api/genres/{}/'.format(self.first_genre.pk))
        self.assertEqual(response.status_code, 204)

    def test_http_delete_will_remove_first_genre_and_return_empty_content(self):
        response = self.client.delete('/api/genres/{}/'.format(self.first_genre.pk))
        self.assertEqual(response.content, '')

    def test_http_delete_will_return_404_when_incorrect_id_used_to_delete_genre(self):
        response = self.client.delete('/api/genres/999999999999999999/')
        self.assertEqual(response.status_code, 404)

class MovieTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(username='myname',\
            email='email@email.com', password='123456')
        self.client.login(username=self.admin.username, password='123456')

        self.first_genre, self.second_genre, self.third_genre, self.fourth_genre, \
        self.fifth_genre, self.sixth_genre = add_genres()
        self.first_movie, self.second_movie = add_movies()
        self.first_movie.genre.add(self.first_genre, self.second_genre, 
            self.third_genre, self.fourth_genre)
        self.second_movie.genre.add(self.first_genre, self.fifth_genre, 
            self.third_genre, self.sixth_genre)
        
    def tearDown(self):
        self.client.logout()  

    def test_http_get_retrieves_list_of_movies_and_returns_200(self):
        response = self.client.get('/api/movies/')
        movies = json.loads(response.content)
        self.assertEqual(response.status_code, 200)

    def test_http_get_will_return_json_object_for_each_movie(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(len(response.data['results']), 2)

    def test_detail_movies_endpoint_returns_attributes_for_given_movie_id(self):
        response = self.client.get('/api/movies/{}/'.format(self.first_movie.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'popularity_99': 83.0,
            'director': 'Victor Fleming',
            'genre': ['Adventure','Family','Fantasy','Musical'],
            'imdb_score': 8.3,
            'name': 'The Wizard of Oz',
            'id' : 1
            })

    def test_http_post_will_create_movie_and_return_201(self):
        data = {
            'popularity_99': 80.0,
            'director': 'Merian C. Cooper',
            'genre': ['Adventure','Fantasy'],
            'imdb_score': 8.0,
            'name': 'King Kong'
            }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, 201)        

    def test_http_post_will_create_movie_and_return_created_movie_json(self):
        data = {
            'popularity_99': 80.0,
            'director': 'Merian C. Cooper',
            'genre': ['Adventure','Fantasy'],
            'imdb_score': 8.0,
            'name': 'King Kong'
            }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.data['genre'], ['Adventure','Fantasy'])

    def test_http_post_without_data_returns_400(self):
        response = self.client.post('/api/movies/', {})
        self.assertEqual(response.status_code, 400)

    def test_http_put_will_update_first_movie_and_return_200(self):
        data = {
            'popularity_99': 83.0,
            'director': 'Ian Fleming',
            'genre': ['Adventure','Family','Fantasy','Musical'],
            'imdb_score': 8.3,
            'name': 'The Wizard of Oz'
            }
        response = self.client.put('/api/movies/{}/'.format(self.first_movie.pk), data)
        self.assertEqual(response.status_code, 200)

    def test_http_put_will_update_first_movie_and_return_updated_movie_json(self):
        data = {
            'popularity_99': 83.0,
            'director': 'Ian Fleming',
            'genre': ['Adventure','Family','Fantasy','Musical'],
            'imdb_score': 8.3,
            'name': 'The Wizard of Oz'
            }
        response = self.client.put('/api/movies/{}/'.format(self.first_movie.pk), data)
        self.assertEqual(response.data['director'], 'Ian Fleming')

    def test_http_delete_will_remove_first_movie_and_return_204(self):
        response = self.client.delete('/api/movies/{}/'.format(self.first_movie.pk))
        self.assertEqual(response.status_code, 204)

    def test_http_delete_will_remove_first_movie_and_return_empty_content(self):
        response = self.client.delete('/api/movies/{}/'.format(self.first_movie.pk))
        self.assertEqual(response.content, '')

    def test_http_delete_will_return_404_when_incorrect_id_used_to_delete_genre(self):
        response = self.client.delete('/api/movies/999999999999999999/')
        self.assertEqual(response.status_code, 404) 