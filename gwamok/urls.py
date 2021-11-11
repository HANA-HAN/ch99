from django.urls import path
from gwamok.views import GwamokLV, GwamokDV
from gwamok import views

app_name = 'gwamok'
urlpatterns = [
    path('', GwamokLV.as_view(), name='index'),
    path('<int:pk>/', GwamokDV.as_view(), name='gwamok_detail'),
    path('add/', views.GwamokCreateView.as_view(),name="add"),
    path('<int:pk>/update/', views.GwamokUpdateView.as_view(), name="update"),
]