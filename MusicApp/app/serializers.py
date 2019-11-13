from rest_framework import serializers
from .models import Musician, Album, AlbumStatistic


class MusicianSerializers(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ["first_name", "last_name", "instrument"]


class AlbumSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ["artist", "name", "release_date", "num_stars"]


class AlbumStatisticSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlbumStatistic
        fields = ["album", "views", "like", "comment"]
