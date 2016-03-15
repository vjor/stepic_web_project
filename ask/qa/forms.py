from django.db import models
from django import forms
from .models import Question,Answer

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
    question  = forms.IntegerField()

    def __init__(self, *args, **kwargs):
	super(AnswerForm, self).__init__(*args, **kwargs)

    def clean_text(self):
	text = self.cleaned_data['text']
	if len(text)>3000:
	    raise forms.ValidationError("Error long text")
	return text +   "\n!Thank you for your Answer!."

    def clean_question(self):
	question = self.cleaned_data['question']
	try:
           qs = Question.objects.get(id=question)
	except Question.DoesNotExist:
	     raise forms.ValidationError("not found question %d" %question)
	return qs

    def save(self):
	ans = Answer(**self.cleaned_data)
	ans.save()
	return ans
