from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Musician, Album, AlbumStatistic
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    MusicianSerializers,
    AlbumSerializers,
    AlbumStatisticSerializers,
)


class MusicianViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers


class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers


class AlbumStatisticViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = AlbumStatistic.objects.all()
    serializer_class = AlbumStatisticSerializers
