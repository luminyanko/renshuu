from django.db import models

# Create your models here.


class Task(models.Model):
    question = models.TextField('Question')
    answer = models.TextField('Answer')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

