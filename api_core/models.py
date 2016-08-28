from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
import mongoengine as mengine

class Genre(models.Model):
    '''
    Model definition for Genre
    '''
    genre_name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return "%s" % self.genre_name

class Movie(models.Model):
    '''
    Model definition for Movie

    '''

    name = models.CharField(max_length=200, 
        verbose_name='Name')
    director = models.CharField(max_length=200, 
        default='null', 
        verbose_name='Director')
    imdb_score = models.FloatField(default=0, 
        verbose_name='IMDB Score', validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    popularity_99 = models.FloatField(default=0, 
        verbose_name='99Popularity', validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    genre = models.ManyToManyField(Genre, related_name='movies', verbose_name='Genre')

    class Meta:
    	ordering = ('name',)
        unique_together = ('name', 'director')

    def __unicode__(self):
    	return "%s" % self.name

class User(mengine.Document):
    """
    User model
    """
    uid = mengine.SequenceField()
    first_name = mengine.StringField()
    last_name = mengine.StringField()
    email = mengine.EmailField(unique=False)
    mobile = mengine.StringField(unique=True)
    password = mengine.StringField()