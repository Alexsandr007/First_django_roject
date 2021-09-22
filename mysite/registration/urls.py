from django.urls import path
from .views import * 


app_name = 'registration'
urlpatterns = [
    # post views
    path('', RegisterUser.as_view(), name='registration'),
]  