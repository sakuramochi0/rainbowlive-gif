import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Gif, Tag


def index(request):
    return HttpResponseRedirect(reverse('page', args=[1]))


def page(request, page):
    paginator = Paginator(Gif.objects.all(), 20)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = Paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.count())

    gifs = page.object_list
    tags = Tag.objects.all()
    return render(request, 'main/index.html', {'gifs': gifs, 'tags': tags, 'page': page})


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