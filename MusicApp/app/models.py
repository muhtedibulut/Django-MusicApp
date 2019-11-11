from django.db import models

# Create your models here.
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


    def __str__(self):
        return "{} - {} - {}".format(self.first_name, self.last_name, self.instrument)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


    def __str__(self):
        return "{} - {} - {}".format(self.artist, self.name, self.release_date, self.num_stars)


class AlbumStatistic(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    views = models.IntegerField()
    like = models.IntegerField()
    comment = models.IntegerField()


    def __str__(self):
        return "{} - {} - {} - {}".format(self.album, self.views, self.like, self.comment)
