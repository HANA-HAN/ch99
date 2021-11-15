from django.urls import path
from gwamok.views import GwamokLV, GwamokDV, DetailView, ListView
from gwamok import views
from gwamok.models import Gwamok, Sugang

app_name = 'gwamok'
urlpatterns = [
    path('', ListView.as_view(model=Gwamok), name='index'),
    path('sugang', ListView.as_view(model=Sugang), name='sugang_list'),
    path('gwamok/<int:pk>/', DetailView.as_view(model=Gwamok), name='gwamok_detail'),
    path('sugang/<int:pk>/', DetailView.as_view(model=Sugang), name='sugang_detail'),
    path('gwamok/add/', views.GwamokCreateView.as_view(),name="gwamok_add"),
    path('gwamok/<int:pk>/update/', views.GwamokUpdateView.as_view(), name="gwamok_update"),
    path('sugang/add/', views.SugangCreateView.as_view(), name="sugang_add"),
    path('sugang/<int:pk>/update/', views.SugangUpdateView.as_view(), name="sugang_update"),
]