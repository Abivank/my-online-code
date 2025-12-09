from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name

class Country(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='countries')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='genres')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
