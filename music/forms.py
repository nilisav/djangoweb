from django import forms
from .models import Song
from .models import Author
from .models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'genre', 'author']
