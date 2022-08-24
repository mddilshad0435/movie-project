from pyexpat import model
from django.db import models
from accounts.models import User

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField(default=None)
    
    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    genres = models.CharField(max_length=100,null=True,blank=True) 
    description = models.TextField()
    uuid = models.CharField(max_length=150,unique=True)

    def __str__(self) -> str:
        return self.title

class CountRequests(models.Model):
    request = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.count)