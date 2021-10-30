from django.urls import path
from phone.views import PhoneLV, PhoneDV
from phone import views

app_name='phone'
urlpatterns = [
    path('', PhoneLV.as_view(), name='index'),
    path('<int:pk>', PhoneDV.as_view(), name='phone_detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
    path('add/', views.PhoneCreateView.as_view(),name="add"),
    path('change/', views.PhoneChangeLV.as_view(),name="change"),
    path('<int:pk>/update/', views.PhoneUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.PhoneDeleteView.as_view(), name="delete"),
]

