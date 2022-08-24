from django.contrib import admin
from .models import Movie,Collection, CountRequests

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','genres','uuid']

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id','user','name']
    
admin.site.register(Movie,MovieAdmin)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(CountRequests)