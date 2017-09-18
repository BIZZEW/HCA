from django.db import models
from django.core.urlresolvers import reverse


# Red pk 1
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('health:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class HealthData(models.Model):
    heart_rate = models.IntegerField()
    weight = models.FloatField(max_length=500)
    temperature = models.FloatField(max_length=100)
    note = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('health:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.heart_rate + ' - ' + self.weight


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
