# quiz/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/quiz/(?P<room_name>[^/]+)-(?P<user_name>[^/]+)/$', consumers.QuizConsumer),
]