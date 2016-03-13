from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Question (models.Model):
    title = models.CharField(max_length=255)
    text  = models.TextField()
    added_at = models.DateTimeField(null=False,blank=True)
    rating   = models.IntegerField()
    author = models.CharField(max_length=255)
    likes =  models.ForeignKey(User)

    def __unicode__(self):
	return self.title
    class Meta:
	ordering = ['-added_at']

class Answer (models.Model):
    text  = models.TextField()
    added_at = models.DateTimeField(null=False,blank=True)
    author = models.CharField(max_length=255)
    question   = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    class Meta:
	ordering = ['-added_at']

