from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Lesson


class LessonListView(ListView):
    model = Lesson
    template_name = 'lessons/lessons.html'
    context_object_name = 'lessons'
    ordering = ['-date_created']


def lesson(request):
    context = {
        'lessons': Lesson.objects.all()
    }
    return render(request, 'lessons.html', context)
