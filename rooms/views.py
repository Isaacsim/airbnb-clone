
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render
from . import models

# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

class RoomDetail(DetailView):

    model = models.Room

    

