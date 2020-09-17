from django.urls import path
from .views import HomePage

app_name = 'Home'

urlpatterns = [
    path('', HomePage, name='Home'),
    ]