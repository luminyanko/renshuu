from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
# dictionary of words, created by user
class Dictionary(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateField(default=timezone.now().date())
    rate = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.name})'

    class Meta:
        verbose_name = "Dictionary"
        verbose_name_plural = "Dictionaries"

    def get_absolute_url(self):
        return reverse('dictionary-detail', kwargs={'pk': self.pk})


# each question in dictionary
class Task(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    question = models.CharField('Question', max_length=150)
    answer = models.TextField('Answer', max_length=150)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['question']
