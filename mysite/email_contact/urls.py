from django.urls import path
from . import views 




app_name = 'contact'
urlpatterns = [
    # post views
    path('', views.contact_page, name='contact'),
    path('send', views.send, name='send'),
]  