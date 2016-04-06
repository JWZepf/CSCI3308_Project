from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Marker(models.Model):
	# all are charfields:
	# https://docs.djangoproject.com/en/1.9/ref/models/fields/#charfield
	# that way we can plug them directly into the javascript as text
	latitude = models.CharField(max_length=100)
	longitude = models.CharField(max_length=100)
	longTitle = models.CharField(max_length=300)
	shortTitle = models.CharField(max_length=50)
	redditLink = models.CharField(max_length=200)
	imageLink = models.CharField(max_length=300)
