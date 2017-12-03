#!/usr/bin/env python3
from get_tweepy import get_api
from tweepy import Cursor
from attrdict import AttrDict
import os
from glob import glob
from main.models import Gif

api = get_api('skrmch_rhythpri')
sn = 'rainbowlive_gif'
directory = '../gifs/'

def get_url(t):
    t = AttrDict(t._json)
    if not 'extended_entities' in t:
        return None
    return t.extended_entities.media[0].video_info.variants[0].url


def download(url):
    base = os.path.basename(url)
    path = os.path.join(directory, base)
    if os.path.exists(path):
       return False
    r = requests.get(url)
    with open(path, 'bw') as f:
        f.write(r.content)
    return True


print('Fetching tweets @rainbowlive_gif...')
ts = [t for t in Cursor(api.user_timeline, screen_name='rainbowlive_gif',count=200).items()]
print('Get {} tweets'.format(len(ts)))

print('Downloading mp4...')
count = 0
for t in ts:
    url = get_url(t)
    if not url:
        continue
    r = download(url)
    if r:
        print(url)
        count += 1
print('Download {} video'.format(count))


print('Creating Gif objects...')
count = 0
fs = [os.path.basename(f) for f in glob('../gifs/*.mp4')]
for f in fs:
    match = Gif.objects.filter(filename=f)
    if not match.count():
        gif = Gif.objects.create(filename=f)
        print(f)
        count += 1
print('Create {} Gif objects'.format(count))
