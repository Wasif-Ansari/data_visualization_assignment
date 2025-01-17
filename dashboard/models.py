from django.db import models

class DataPoint(models.Model):
    end_year = models.CharField(max_length=10, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100, blank=True)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=10, blank=True)
    impact = models.CharField(max_length=10, blank=True)
    added = models.CharField(max_length=100)
    published = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.TextField()
    likelihood = models.IntegerField()
