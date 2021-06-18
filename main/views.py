from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Task, Dictionary
from .forms import TaskForm, DictionaryForm


class DictionaryListView(ListView):
    model = Dictionary
    template_name = 'main/practice.html'
    context_object_name = 'dicts'
    ordering = ['-created']


class DictionaryDetailView(DetailView):
    model = Dictionary


class DictionaryCreateView(LoginRequiredMixin, CreateView):
    model = Dictionary
    fields = ['name']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DictionaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Dictionary
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        dictionary = self.get_object()
        if self.request.user == dictionary.creator:
            return True
        return False


class DictionaryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Dictionary
    success_url = '/practice'

    def test_func(self):
        dictionary = self.get_object()
        if self.request.user == dictionary.creator:
            return True
        return False


def index(request):
    return render(request, 'main/index.html')


def practice(request):
    context = {
        'dicts': Dictionary.objects.all(),
        'user': User
    }
    return render(request, 'main/practice.html', context)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = DictionaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Invalid input'
    form = DictionaryForm()
    context = {
        'form': form
    }
    return render(request, 'main/dictionary_form.html', context)
