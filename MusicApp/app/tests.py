from django.test import TestCase
from .models import Musician, Album, AlbumStatistic


class MusicianTest(TestCase):
    def create_musician(self, first_name="a", last_name="b", instrument="a"):
        return Musician(
            first_name=first_name, last_name=last_name, instrument=instrument
        )

    def test_musician_creation1(self):
        musician = self.create_musician()
        self.assertTrue(isinstance(musician, Musician))

    def test_musician_creation2(self):
        musician = self.create_musician()
        self.assertEqual(musician.__str__(), musician.last_name)


class AlbumTest(TestCase):
    def create_album(self, name="a", num_stars=10):
        return Album(name=name, num_stars=num_stars)

    def test_album_creation1(self):
        album = self.create_album()
        self.assertTrue(isinstance(album, Album))

    def test_album_creation1(self):
        album = self.create_album()
        self.assertEqual(album.__str__(), album.name)


class AlbumStatisticTest(TestCase):
    def create_album_statistic(self, views=10, like=10, comment=100):
        return AlbumStatistic(views=views, like=like, comment=comment)

    def test_album_statstic_creation1(self):
        album_statistic = self.create_album_statistic()
        self.assertTrue(isinstance(album_statistic, AlbumStatistic))

    def test_album_statstic_creation1(self):
        album_statistic = self.create_album_statistic()
        self.assertEqual(album_statistic.__str__(), album_statistic.views)


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)
