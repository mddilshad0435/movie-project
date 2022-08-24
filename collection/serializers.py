from dataclasses import fields
from rest_framework import serializers
from .models import Movie,Collection, CountRequests

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title','uuid','description']

class CollectionSerializer(serializers.ModelSerializer):
    collections = serializers.SerializerMethodField()
    movies = serializers.ListField(write_only=True)
    favourite_genres = serializers.SerializerMethodField()

    def get_collections(self,obj):
        query = Movie.objects.filter(collection=obj)
        return MovieSerializer(instance=query, many=True).data
    def get_favourite_genres(self,obj):
        query = Movie.objects.filter(collection=obj).values_list('genres',flat=True)[:3]
        return ','.join(query)
    class Meta:
        model = Collection
        fields = ['name','description','collections','movies','favourite_genres']
        
    def create(self,validate_data):
        movies = validate_data.pop('movies')
        user = self.context['request'].user
        collection = Collection.objects.create(user=user, **validate_data)
        collection.save()
        movies_list = []
        if movies:
            for movie in movies:
                movies_list.append(Movie(collection=collection, **movie))
            Movie.objects.bulk_create(movies_list)
        return collection

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountRequests
        fields = ['count']