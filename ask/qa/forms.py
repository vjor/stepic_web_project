from django.db import models
from django import forms
from .models import *

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    def clean_text(self):
	text = self.cleaned_data['text']
	if len(text)>3000:
	    raise forms.ValidationError("Error")
	return text +   "\n!Thank you for your question!."
    def save(self):
	qs = Question(**self.cleaned_data)
	qs.save()
	return qs

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question_id  =forms.IntegerField()
    def clean_text(self):
	text = self.cleaned_data['text']
	if len(text)>3000:
	    raise forms.ValidationError("Error long text")
	return text +   "\n!Thank you for your Answer!."
    def clean_question_id(self):
	question_id = self.cleaned_data['question_id']
	try:
           qs = Question.objects.get(id=question_id) 
	except Question.DoesNotExist:
	     raise forms.ValidationError("not found question %d" %question_id)
	return question_id
    def save(self):
	ans = Answer(**self.cleaned_data)
	ans.save()
	return ans
