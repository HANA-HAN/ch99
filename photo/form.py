from django import forms
from django.forms import inlineformset_factory
from photo.models import Album, Photo

class PhotoSearchForm(forms.Form):
    search_word=forms.CharField(label='Search Word')

PhotoInlineFormSet = inlineformset_factory(Album, Photo, fields=['image','title','description'], extra=2)

