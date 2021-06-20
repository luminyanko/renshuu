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


class LessonDetailView(DetailView):
    model = Lesson


class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lesson
    fields = ['title', 'content', 'tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lesson
    fields = ['title', 'content', 'tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class LessonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lesson
    success_url = '/lessons'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

