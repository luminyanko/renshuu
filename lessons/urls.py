from django.urls import path
from .views import (
    LessonListView,
)
from . import views

urlpatterns = [
    path('lessons', LessonListView.as_view(), name='lessons'),

]