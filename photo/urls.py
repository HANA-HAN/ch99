from django.urls import path
from photo import views
from photo.models import Album, Photo
from photo.views import ListView, DetailView

app_name='photo'
urlpatterns=[
    path('', ListView.as_view(model=Album), name='index'),
    path('album',ListView.as_view(model=Album), name='album_list'),
    path('album/<int:pk>/', DetailView.as_view(model=Album), name='album_detail'),
    path('photo/<int:pk>/', DetailView.as_view(model=Photo),name='photo_detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]