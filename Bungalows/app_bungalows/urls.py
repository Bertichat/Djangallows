from django.urls import path
from app_bungalows.views import *

app_name='app_bungalows'

urlpatterns = [
    path('BungalowsList', BungalowsList,  name='BungalowsList'),
    path('BungalowsChoice', BungalowsChoice,  name='BungalowsChoice'),
    path('BungalowsMaj', BungalowsMaj,  name='BungalowsMaj'),
    path('BungalowsMajSetItems', BungalowsMajSetItems,  name='BungalowsMajSetItems'),
]