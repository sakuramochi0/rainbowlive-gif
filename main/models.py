from django.db import models


class Gif(models.Model):
    filename = models.FilePathField
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    gif = models.ManyToManyField(Gif, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
