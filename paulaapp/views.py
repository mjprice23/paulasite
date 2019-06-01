from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Prospect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Prospect


class ProspectListView(ListView):
    model = Prospect


class ProspectDetailView(UpdateView):
    model = Prospect
    fields = '__all__'
    template_name = 'paulaapp/prospect_form.html'
    success_url = reverse_lazy('prospect-list')


class ProspectAddView(CreateView):
    model = Prospect
    fields = '__all__'
    template_name = 'paulaapp/prospect_form.html'
    success_url = reverse_lazy('prospect-list')


class ProspectDeleteView(DeleteView):
    model = Prospect
    fields = '__all__'
    template_name = 'paulaapp/prospect_confirm_delete.html'
    success_url = reverse_lazy('prospect-list')

# Create your views here.
