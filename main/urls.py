from django.urls import path
from .views import (
    DictionaryListView,
    DictionaryDetailView,
    DictionaryCreateView,
    DictionaryUpdateView,
    DictionaryDeleteView
)
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('practice', DictionaryListView.as_view(), name='practice'),
    path('practice/new', DictionaryCreateView.as_view(), name='dictionary-create'),
    path('practice/<pk>', DictionaryDetailView.as_view(), name='dictionary-detail'),
    path('practice/<pk>/update', DictionaryUpdateView.as_view(), name='dictionary-update'),
    path('practice/<pk>/delete', DictionaryDeleteView.as_view(), name='dictionary-delete'),
]