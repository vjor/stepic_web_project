from django.db import models
from django import forms
from .models import Question,Answer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


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



class SignForm(forms.Form):
    username  = forms.CharField(max_length=20)
    email     =  forms.EmailField()
    password  = forms.CharField(max_length=16)

    def clean_username(self):
	username = self.cleaned_data['username']
	try:
	    User.objects.get(username=username)         
	except User.DoesNotExist:
        	return username
	raise forms.ValidationError("User is register %s" %username)

    def clean_email(self):
	email = self.cleaned_data['email']
        try:
    	  User.objects.get(email=email)
        except User.DoesNotExist:
    	      return email
        raise forms.ValidationError(("email alredy exists, please new  email"))

    def save(self):

	username = self.cleaned_data['username']
	email = self.cleaned_data['email']
        password = self.cleaned_data['password']
	
	user = User.objects.create_user(username, email,password)
	user.save()
	return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField( widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': ("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': ("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
	username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
         if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
