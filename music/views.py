from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Song
from .forms import GenreForm
from .forms import AuthorForm
from .forms import SongForm


def index(request):
    genre_form = None
    author_form = None
    song_form = None
    answer = dict()
    song_list = Song.objects.all()
    template = loader.get_template('song/index.html')

    if request.method == 'POST':
        if 'genre_send' in request.POST:
            genre_form = GenreForm(request.POST)
            genre_form.save()
            answer["genre"] = "Сохранено!"
        if 'author_send' in request.POST:
            author_form = AuthorForm(request.POST)
            author_form.save()
            answer["author"] = "Сохранено!"
        if 'song_send' in request.POST:
            song_form = SongForm(request.POST)
            song_form.save()
            answer["song"] = "Сохранено!"

    if genre_form is None:
        genre_form = GenreForm()
    if author_form is None:
        author_form = AuthorForm()
    if song_form is None:
        song_form = SongForm()

    context = {
        'song_list': song_list,
        'genre_form': genre_form,
        'author_form': author_form,
        'song_form': song_form,
    }

    if len(answer) > 0:
        context['answer'] = answer

    return HttpResponse(template.render(context, request))


def detail(request, song_id):
    song = Song.objects.get(pk=song_id)

    if request.method == 'POST':
        song_form = SongForm(request.POST, instance=song)
        song_form.save()
        answer = "Сохранено!"
    else:
        song_form = SongForm(instance=song)
        answer = None

    context = {
        'song': song,
        'song_form': song_form
    }

    if answer is not None:
        context['answer'] = answer
    template = loader.get_template('song/detail.html')

    return HttpResponse(template.render(context, request))
