from rest_framework import serializers

from api_core.models import Movie 
from api_core.models import Genre
from api_core.models import User

class GenreSerializer(serializers.ModelSerializer):
	'''
	Serializer for the Genre Model
	'''

	class Meta:
		model = Genre
		fields = ('id','genre_name',)
		read_only_fields = ('id')

class MovieSerializer(serializers.ModelSerializer):
	'''
	Serializer for the Movie Model
	'''	
	genre = serializers.SlugRelatedField(many=True, 
		queryset=Genre.objects.all(),
		slug_field='genre_name')
	
	class Meta:
		model = Movie
		fields = ('id', 'name', 'director', 'imdb_score', 'popularity_99', 'genre')
		read_only_fields = ('id')

	def validate_genre(self, value):
		'''
		Check that list of genres is not empty
		'''
		if not value:
			raise serializers.ValidationError("List of Genres cannot be empty")
		return value

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email', 'mobile')