from django.urls import path
from .views import Register

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'Profile'
urlpatterns = [
    path('Register/', Register, name='Register'),
    path('Login/', LoginView.as_view(template_name='Profile/Login.html'), name='Login'),
    path('Logout/', LogoutView.as_view(template_name='Profile/Logout.html'),name='Logout'),
]