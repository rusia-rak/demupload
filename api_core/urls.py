from api_core.views import MovieViewSet 
from api_core.views import GenreViewSet
from api_core.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', MovieViewSet, base_name='movies_api')
router.register(r'genres', GenreViewSet, base_name='genres_api')
router.register(r'users', UserViewSet, base_name='users_api')