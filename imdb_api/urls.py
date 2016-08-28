from django.conf.urls import url
from django.conf.urls import include

from api_core.urls import router

urlpatterns = [
	url(r'^api/', include(router.urls))]
