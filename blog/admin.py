from django.contrib import admin
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {
        "slug" : ["title"],
    }

admin.site.register(models.Comment)
admin.site.register(models.Category)