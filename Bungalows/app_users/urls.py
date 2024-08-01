from django.urls import path
from app_users.views import *
from allauth.account.views import LoginView, LogoutView

app_name='app_users'

urlpatterns = [
    path('', Login,  name='Login'),
    path('logout', Logout,  name='Logout'),
    # path('Login', LoginView.as_view(),  name='Login'),

    path('Welcome', Welcome,  name='Welcome'),
]