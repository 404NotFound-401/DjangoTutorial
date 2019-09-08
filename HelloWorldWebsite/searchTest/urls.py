# urls relation for the search testing page

from django.urls import path
from . import views
urlpatterns = [
    path('', views.Search.as_view(), name='mainpage'),
]
