from django.urls import path
from .views import DictionaryListView, DictionaryDetailView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('practice', DictionaryListView.as_view(), name='practice'),
    path('practice/<pk>', DictionaryDetailView.as_view(), name='dictionary-detail'),
]