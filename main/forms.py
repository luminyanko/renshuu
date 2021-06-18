from .models import Task, Dictionary
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['question', 'answer']
        widgets = {
            'question': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter question'
            }),
            'answer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter answer'
            }),
        }


class DictionaryForm(ModelForm):
    class Meta:
        model = Dictionary
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter dictionary name',
            })
        }
