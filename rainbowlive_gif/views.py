from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F, Count

from .models import Gif, Tag


def index(request):
    tags = Tag.objects.all()
    tag_gif_list = []
    for tag in tags:
        # 多人数が映っているタグを選択すると同じGIFが重複してしまうので
        # タグを1つだけ持っているGIFを選択する
        gif = Gif.objects.annotate(num_tags=Count(F('tags'))).filter(num_tags=1, tags=tag).first()
        if not gif:
            # tagが1つだけのgifがない時は複数人を許す
            gif = Gif.objects.filter(tags=tag).first()
        if not gif:
            # gifが0個の場合はスキップする
            continue
        tag_gif = (tag, gif)
        tag_gif_list.append(tag_gif)
    return render(request, 'rainbowlive_gif/index.html', {'tag_gif_list': tag_gif_list})

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
    return render(request, 'rainbowlive_gif/page.html', {'gifs': gifs, 'tags': tags, 'page': page})


def tag(request, tag_name, page_num=1):
    gifs = Gif.objects.filter(tags__name=tag_name)
    tag = Tag.objects.get(name=tag_name)
    paginator = Paginator(gifs, 20)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = Paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.count())

    gifs = page.object_list
    tags = Tag.objects.all()
    return render(request, 'rainbowlive_gif/tag.html', {'gifs': gifs, 'tags': tags, 'page': page, 'tag': tag})


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
