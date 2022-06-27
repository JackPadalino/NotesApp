from optparse import TitledHelpFormatter
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Category,Note

class CategoryCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title')
    class Meta:
        model = Category
        fields = ['title']

class NoteCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title')
    content = forms.CharField(widget=forms.Textarea,label="What's this note about?")
    class Meta:
        model = Note
        fields = ['title','content']