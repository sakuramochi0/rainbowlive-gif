from django.contrib import admin
from .models import Gif, Tag


class GifAdmin(admin.ModelAdmin):
    model = Gif
    filter_horizontal = ('tags', )


admin.site.register(Tag)
admin.site.register(Gif, GifAdmin)
