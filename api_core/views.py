import django_filters

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin 
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin 
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin

from api_core.models import Movie
from api_core.models import Genre
from api_core.models import User
from api_core.serializers import MovieSerializer
from api_core.serializers import GenreSerializer
from api_core.serializers import UserSerializer
from api_core.permissions import IsAdminOrReadOnly

class MovieFilter(django_filters.FilterSet):
	'''
	Filter definitions for the Movies
	'''
	min_score = django_filters.NumberFilter(name="imdb_score", lookup_type='gte')
	max_score = django_filters.NumberFilter(name="imdb_score", lookup_type='lte')
	genre = django_filters.CharFilter(name="genre__genre_name")
	class Meta:
	    model = Movie
	    fields = ['name', 'director', 'min_score', 'max_score','genre']


class GenreViewSet(viewsets.GenericViewSet, ListModelMixin, 
	CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
	'''
	This endpoint presents all the Genres in the System
	'''	
	permission_classes = [IsAdminOrReadOnly,]
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('genre_name',)

class MovieViewSet(viewsets.GenericViewSet, ListModelMixin, 
	CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
	'''
	This endpoint presents all the Movies in the System.
	
	To view the details of a Movie Instance suffix the endpoint with the **Movie ID**.
	
	To search for a *Movie* or *Director*, suffix the endpoint with **?search=**

	'''	

	permission_classes = [IsAdminOrReadOnly,]
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	filter_class = MovieFilter
	filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
	search_fields = ('name','director',)

class UserViewSet(viewsets.GenericViewSet, ListModelMixin,
	CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):

	permission_classes = [IsAdminOrReadOnly,]
	queryset = User.objects.all()
	serializer_class = UserSerializer
