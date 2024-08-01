from django.urls import path
from app_fournitures.views import *

app_name='app_fournitures'

urlpatterns = [
    path('addFournitureTemplate', addFournitureTemplate,  name='addFournitureTemplate'),
    path('addFourniture', addFourniture,  name='addFourniture'),
    path('updateFourniture/<int:pk>/', updateFourniture,  name='updateFourniture'),
    path('Fourniture_checklist', Fourniture_checklist,  name='Fourniture_checklist'),
    path('Fourniture_diff', Fourniture_diff,  name='Fourniture_diff'),
]