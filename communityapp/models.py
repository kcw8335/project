from django.db import models
from accountsapp.models import User
from django.contrib import auth


class Community(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.CharField(max_length=500)

class Notice(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title