from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    name_ja = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} (#{})'.format(self.name_ja, self.name)


class Gif(models.Model):
    filename = models.CharField(max_length=100, default='')
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_updated_to_giphy = models.BooleanField(default=False)
    tweet_url = models.CharField(max_length=255, default=None)

    def __str__(self):
        tags = ' '.join(['#' + t.name for t in self.tags.all()])
        return '{} ({})'.format(self.filename, tags)
