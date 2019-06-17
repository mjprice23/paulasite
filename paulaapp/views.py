from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Prospect
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


class ProspectListView(ListView):
    model = Prospect

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            q = Q()
            # notes_found = Prospect.objects.filter(notes__icontains=query)
            # fname_found = Prospect.objects.filter(first_name__icontains=query)
            # lname_found = Prospect.objects.filter(last_name__icontains=query)
            q |= Q(notes__icontains=query)
            q |= Q(first_name__icontains=query)
            q |= Q(last_name__icontains=query)
            # found = notes_found.union(fname_found, lname_found).order_by('-date_most_recent_visit').distinct()
            return Prospect.objects.filter(q).distinct()
        else:
            return Prospect.objects.all()


class ProspectDetailView(UpdateView):
    model = Prospect
    fields = '__all__'
    # template_name = 'paulaapp/prospect_form.html'
    template_name = 'paulaapp/prospect_edit.html'
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


class HomePageView(TemplateView):
    template_name = 'paulaapp/home_page.html'


class ToDoListView(ListView):
    model = Prospect
    template_name = 'paulaapp/to_do_list.html'

    def get_queryset(self): #gets everything shown on page
        queryset = super(ToDoListView, self).get_queryset()
        queryset = queryset.order_by('action_date')
        return queryset




# Create your views here.
