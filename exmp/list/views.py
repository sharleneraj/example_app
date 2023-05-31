from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Person
from .forms import PersonForm
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'list/base.html')


class PersonListView(ListView):
    model = Person
    template_name = 'list/person_list.html'
    context_object_name = 'persons'


class PersonCreateView(CreateView):
    model = Person
    template_name = 'list/person_form.html'
    form_class = PersonForm
    success_url = reverse_lazy('person-list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'list/person_form.html'
    success_url = reverse_lazy('person-list')


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'list/person_confirm_delete.html'
    success_url = reverse_lazy('person-list')


class PersonDetailView(DetailView):
    model = Person
    template_name = 'list/person_detail.html'
    context_object_name = 'person'






