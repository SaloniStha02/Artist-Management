from django.urls import path
from .views import SongList,SongDetailList
urlpatterns =[
    path("songs/",SongList.as_view(), name="song-view"),
    path("songs/<int:pk>/",SongDetailList.as_view(), name="song-detail"),
]