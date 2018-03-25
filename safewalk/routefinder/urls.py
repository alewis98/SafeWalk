from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
#    path('request/', views.authorize, name='authorize'),
    path('', views.login, name='login'),
    path('login/', login, {'template_name': 'routefinder/login.html'}),
    path('get_name/', views.get_name, name='get_name'),
]