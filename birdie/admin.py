from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    model = models.Post
    list_display = ('excerpt',)

    def excerpt(self, obj):
        return obj.get_excerpt(5)
