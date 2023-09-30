# from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

# Create your views here.

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['work_type']
    search_fields = ['artist__name']

class ArtistRegistrationView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
