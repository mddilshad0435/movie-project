from django.urls import path
from . import views
urlpatterns = [
    path('movies/', views.MovieList.as_view(),name="get-movie-list"),
    path('collection/',views.CollectionView.as_view(),name="collection"),
    path('collection/<str:uuid>/',views.MovieView.as_view(),name="collection-detail"),
    path('request-count/',views.CountRequestView.as_view(), name='request-count'),
    path('request-count/reset/',views.CountRequestPostView.as_view(), name='request-count-reset')
]