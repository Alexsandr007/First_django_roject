from django.urls import path
from . import views 



app_name = 'cars'
urlpatterns = [
    # post views
    path('car-single/<int:post_id>', views.car_single_page, name='car_single'),
    path('', views.post_list, name='post_list'),
]  