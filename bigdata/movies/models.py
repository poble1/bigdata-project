# from django.db import models
from djongo import models
from django.conf import settings as djangoSettings
import os,csv
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

    def count_genres(self, queryset):
        genres = []

        for movie in queryset:
            m_genres = movie.genres(manager='objects').all()
            for genre in m_genres:
                if len(genres) == 0:
                    new_one = {'genre' : genre.name, 'count' : 1}
                    genres.append(new_one)
                    print(genre.name + " Added // genres len : " + str(len(genres)))
                else:
                    length = len(genres)
                    count = 1
                    for g in genres:
                        if genre.name == g['genre']:
                            g['count'] += 1  
                            print(genre.name + " + 1")
                            break
                        elif count == length:
                            new_one = {'genre' : genre.name, 'count' : 1}
                            genres.append(new_one)
                            print(genre.name + " Added // genres len : " + str(len(genres)))
                            break
                        else:
                            count+=1
        import csv    
        f = open('/Users/move0/dev/django/bigdata/bigdata/static/movies/data/recent_genre.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow(['name', 'count'])
        for line in genres:
            newline = [line['genre'], line['count']]
            wr.writerow(newline)
        f.close()
        return

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

class User(models.Model):
    name = models.CharField(max_length=200)

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="ratings")
    rating = models.FloatField(default=0)
