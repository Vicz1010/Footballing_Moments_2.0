from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    age = models.CharField(max_length = 150)
    country = models.CharField(max_length = 150)
    title = models.CharField(max_length = 150)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('thread_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title + ' | ' + str(self.name)


class Comment(models.Model):
    thread = models.ForeignKey('newapp.Thread', related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('thread_list')

    def __str__(self):
        return self.text
