from django import forms
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('name','age','country','title','text',)

        widgets = {
            'age': forms.TextInput(attrs={'class': 'textinputclass'}),
            'country': forms.TextInput(attrs={'class': 'textinputclass'}),
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'textinputclass'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('name','text',)

    widgets = {
        'text': forms.Textarea(attrs={'class': 'textinputclass'}),
    }