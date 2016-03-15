from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Question (models.Model):
    title = models.CharField(max_length=255)
    text  = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating   = models.IntegerField(null=True)
    author = models.CharField(max_length=255,default="1")
    likes =  models.ForeignKey(User, null=True, default=1)

    def __unicode__(self):
	return self.title
    class Meta:
	ordering = ['-added_at']

class Answer (models.Model):
    text  = models.TextField()
    added_at = models.DateTimeField(null=True)
    author = models.CharField(max_length=255,default="1")
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    class Meta:
	ordering = ['-added_at']

