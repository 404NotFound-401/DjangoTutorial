from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Movie
from . import searchapi

# Create your views here.

class Search(generic.DetailView):
    model = Movie
    template_name = 'searchTest.html'

    def get(self, request, *args, **kwargs):
        context = {'movieId':'Please enter the film name'}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'movieName' in request.GET:
            context = getName(request.GET[movieName])
        else:
            print("Wrong act")
            return redirect('mainpage') 
        return render(request, self.template_name, context)

