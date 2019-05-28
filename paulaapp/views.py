from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Prospect


class ProspectListView(ListView):

    model = Prospect




# Create your views here.

