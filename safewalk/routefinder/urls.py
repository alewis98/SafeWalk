from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'routefinder/login.html'})
    path('form/', views.get_name,)
]