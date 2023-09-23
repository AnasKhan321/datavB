from django.db import models

# Create your models here.

class Edata (models.Model):
    end_year = models.CharField(default="", max_length=90)
    intensity =  models.CharField(default="" , max_length=100)
    sector = models.CharField(default="", max_length=190)
    topic = models.CharField(default="" ,max_length=70)
    insight = models.CharField(default="" , max_length=90)
    url = models.CharField(default="" , max_length=500)
    region = models.CharField(default="" , max_length=200)
    start_year = models.CharField(default="" , max_length=120)
    impact = models.CharField(default="" , max_length=120)
    added = models.CharField(default="" , max_length=500)
    published = models.CharField(default="" , max_length=100)
    country  = models.CharField(default="" , max_length=100)
    relevance = models.CharField(default="" ,  max_length=100)
    pestle = models.CharField(default="" , max_length=190)
    source = models.CharField(default="" , max_length=50)
    title = models.CharField(default="" , max_length=500)
    likelihood = models.CharField(default="" ,max_length=100)

    def __str__(self):
        return  self.topic
