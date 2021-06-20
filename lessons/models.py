from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Lesson(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

