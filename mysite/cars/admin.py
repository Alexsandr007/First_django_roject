from django.contrib import admin
from .models import Car,Happy_clients

# Register your models here.
@admin.register(Car)
class CommentAdmin(admin.ModelAdmin): 
    list_display = ('subheading', 'model_for_car') 
    list_filter = ('cost_hour', 'cost_day', 'cost_mounth') 
    search_fields = ('subheading', 'model_for_car') 

admin.site.register(Happy_clients)