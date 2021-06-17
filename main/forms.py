from .models import Task
from django.forms import ModelForm, TextInput


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
