from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import CollectionSerializer,MovieSerializer, CountSerializer
from .models import Collection,Movie, CountRequests

class MovieList(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        url = 'https://demo.credy.in/api/v1/maya/movies/'
        try:
            data = requests.get(url=url).json()
            return Response(data)
        except:
            return Response({'message':"Pleasy retry"})
        
class CollectionView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
class MovieView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    lookup_field = 'uuid'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CountRequestView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        count = CountRequests.objects.all().first()
        serializer = CountSerializer(count)
        return Response({'requests':serializer.data})

class CountRequestPostView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        CountRequests.objects.filter(request='request').update(count=0)
        return Response({'message':'request count reset successfully'})
