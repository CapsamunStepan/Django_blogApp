from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.view_home, name='view_home'),
]