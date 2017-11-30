import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Gif, Tag


def index(request):
    gifs = Gif.objects.all()
    tags = Tag.objects.all()
    return render(request, 'main/index.html', {'gifs': gifs, 'tags': tags})


def update_tag(request):
    tag = request.POST['tag']
    filename = request.POST['filename']
    checked = request.POST['checked']
    if checked == 'true':
        checked = True
    else:
        checked = False

    gif = Gif.objects.get(filename=filename)
    tag = Tag.objects.get(name=tag)
    if checked:
        print('add', tag)
        gif.tags.add(tag)
    else:
        print('remove', tag)
        gif.tags.remove(tag)

    return HttpResponse('')