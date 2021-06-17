from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def practice(request):
    questions = Task.objects.all()
    return render(request, 'main/practice.html', {'questions': questions})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Invalid input'
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
