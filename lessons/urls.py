from django.urls import path
from .views import (
    LessonListView,
    LessonDetailView,
    LessonCreateView,
    LessonUpdateView,
    LessonDeleteView
)
from . import views

urlpatterns = [
    path('lessons', LessonListView.as_view(), name='lessons'),
    path('lessons/new', LessonCreateView.as_view(), name='lesson-create'),
    path('lessons/<pk>', LessonDetailView.as_view(), name='lesson-detail'),
    path('lessons/<pk>/edit', LessonUpdateView.as_view(), name='lesson-edit'),
    path('lessons/<pk>/delete', LessonDeleteView.as_view(), name='lesson-delete'),
]