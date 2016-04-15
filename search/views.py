from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect
import requests

# Create your views here.
def index(request):
	if request.method=="GET":
		form = SearchForm()
		return render(request,'templates/index.html',{'form':form})
	elif request.method=="POST":
		form = SearchForm(request.POST)
		movie = request.POST['name']
		url = 'http://www.omdbapi.com/?t='
		for x in movie.split(' '):
			url += x +'+'

		url +='&y='+request.POST['year']

		#'http://www.omdbapi.com/?t='+movie+'&tomatoes=true'
		r = requests.get(url)
		data = r.json()
		context = {
		'title':data['Title'],
		'plot':data['Plot'],
		'rated':data['Rated'],
		'imdbRating':data['imdbRating'],
		'genre':data['Genre'],
		}

		return render(request,'templates/results.html',context)


# def results(request):
# 	return render(request,'templates/results.html',{})