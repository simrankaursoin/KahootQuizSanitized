# quiz/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quiz/(?P<room_name>[^/]+)-(?P<user_name>[^/]+)/$', views.room, name='room'),
    url(r'^teachers/(?P<room_name>[^/]+)-(?P<user_name>[^/]+)/$', views.teacher_room, name='teachers'),
    url(r'^teachers/(?P<room_name>[^/]+)-(?P<user_name>[^/]+)/bargraph$', views.bargraph_display, name='bargraph'),
]
