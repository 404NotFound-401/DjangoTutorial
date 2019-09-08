from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from . import searchapi

# Create your views here.

class Result(generic.DetailView):
    template_name = 'result.html'

    def post(self, request, *args, **kwargs):
        if 'movieName' in request.GET:
            context = getName(request.GET(movieName))
        else:
            return redirect('searchTest') 
        return render(request, self.template_name, context)