from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Movie

# Create your views here.

class Search(generic.DetailView):
    model = Movie
    template_name = 'searchTest.html'

    def get(self, request, *args, **kwargs):
        context = {'movieId' : ''}
        return render(request, self.template_name)