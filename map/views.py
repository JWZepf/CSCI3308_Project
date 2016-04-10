import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
import praw
import re
import string
import urllib
import json
from geopy.geocoders import Nominatim
from .models import Marker

def index(request):
	marker_list = Marker.objects.all()[:5]
	context = {'marker_list': marker_list}
	return render(request, 'script.js', context)

@staff_member_required
def bot(request):
	user_agent = ("WanderMap 0.1")  # Sets name of User Agent that we will use
	r = praw.Reddit(user_agent = user_agent)
	subreddit = r.get_subreddit("earthporn") # We are looking at /r/earthporn
	for submission in subreddit.get_top(limit = 5,period = 'day'): # Get the top 25 hot posts PERIOD equals previous 24 hours
		value = submission.title
		url_text = submission.url
		marker = Marker()
		marker.latitude = 'none'
		marker.longitude = 'none'
		marker.longTitle = value
		marker.shortTitle = 'none'
		marker.redditLink = 'none'
		marker.imageLink = url_text
		marker.save()
	return render(request, 'script.js')

