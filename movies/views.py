from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import Movies
from movies.serializers import MovieSerializer
from app.permissions import GlobalDefaultPermission


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,) 
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,) 
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer