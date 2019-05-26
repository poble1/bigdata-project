# from django.db import models
from djongo import models
# Create your models here.

class ProductionCompany(models.Model):
    company_id = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductionCountry(models.Model):
    country_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SpokenLanguage(models.Model):
    language_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Collection(models.Model):    
    collection_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    movie_id = models.IntegerField()
    imdb_id = models.CharField(blank=True, max_length=200)
    overview = models.CharField(max_length=200)
    popularity = models.FloatField(default=0)
    poster = models.URLField()
    production_companies = models.ManyToManyField(ProductionCompany)
    production_countries = models.ManyToManyField(ProductionCountry)
    release_date = models.DateField()
    revenue = models.IntegerField(default=0)
    runtime = models.IntegerField(default=0)
    spoken_languages = models.ManyToManyField(SpokenLanguage)
    status = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    video = models.BooleanField()
    genres = models.ManyToManyField(Genre)
    vote_avg = models.FloatField(default=0)
    vote_count = models.IntegerField(default=0)
    original_language = models.CharField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Rating(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.FloatField(default=0)
