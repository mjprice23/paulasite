from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Prospect, Visit
from django.db.models import Q
from .forms import VisitForm, ProspectVisitFormSet
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.contrib.auth.mixins import LoginRequiredMixin


class ProspectListView(LoginRequiredMixin, ListView):
    model = Prospect
    template_name = 'paulaapp/prospect_list.html'
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


class ProspectEditView(LoginRequiredMixin, UpdateView):
    model = Prospect
    fields = '__all__'
    # template_name = 'paulaapp/prospect_form.html'
    template_name = 'paulaapp/prospect_edit.html'
    success_url = reverse_lazy('prospect-list')

    def get(self, request, *args, **kwargs):  # Initialize and pass into context data
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        visits_formset = ProspectVisitFormSet(instance=self.object, prefix='visits_fs')

        formset_dict = {'visits_form': visits_formset}
        return self.render_to_response(
            self.get_context_data(form=form, **formset_dict)
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        visits_formset = ProspectVisitFormSet(self.request.POST, instance=self.object, prefix='visits_fs')

        formset_dict = {'visits_form': visits_formset}
        if form.is_valid() and visits_formset.is_valid():
            return self.form_valid(form, formset_dict)
        else:
            return self.form_invalid(form, formset_dict)

    def form_valid(self, form, formsets):
        self.object = form.save()
        for formset_name in formsets.keys():
            formset = formsets[formset_name]
            formset.instance = self.object  # ties it to the correct Prospect
            formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formsets):
        print('invalid form')
        return self.render_to_response(
            self.get_context_data(form=form, **formsets)
        )

    def get_success_url(self):
        return reverse_lazy('prospect-list')


class ProspectAddView(LoginRequiredMixin, CreateView):
    model = Prospect
    fields = '__all__'
    template_name = 'paulaapp/prospect_form.html'
    success_url = reverse_lazy('prospect-list')


class ProspectDeleteView(LoginRequiredMixin, DeleteView):
    model = Prospect
    fields = '__all__'
    template_name = 'paulaapp/prospect_confirm_delete.html'
    success_url = reverse_lazy('prospect-list')


class ProspectDetailView(LoginRequiredMixin, DetailView):
    model = Prospect
    template_name = 'paulaapp/prospect_details.html'


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'paulaapp/home_page.html'


class ToDoListView(LoginRequiredMixin, ListView):
    model = Prospect
    template_name = 'paulaapp/to_do_list.html'

    def get_queryset(self): #gets everything shown on page
        queryset = super(ToDoListView, self).get_queryset()
        queryset = queryset.order_by('action_date')
        return queryset


class IchijoCardView(LoginRequiredMixin, DetailView):
    model = Prospect

