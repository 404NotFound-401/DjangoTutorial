# urls relation for the search testing page

from django.urls import path
from . import views
urlpatterns = [
    path('', views.Result.as_view(), name='resultpage'),
]