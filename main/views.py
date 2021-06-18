from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Task, Dictionary
from .forms import TaskForm, DictionaryForm


class DictionaryListView(ListView):
    model = Dictionary
    template_name = 'main/practice.html'
    context_object_name = 'dicts'
    ordering = ['-created']


class DictionaryDetailView(DetailView):
    model = Dictionary


def index(request):
    return render(request, 'main/index.html')


def practice(request):
    context = {
        'dicts': Dictionary.objects.all()
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
    return render(request, 'main/create.html', context)
