from django.contrib import admin
from models import *


# Set up the models in admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'article_category', 'published_date',)

    list_filter = ('title','article_category', 'published_date',)


    fieldsets = (
        (None, {'fields': ('title', 'content', 'author', 'article_category')}),
        ('Advanced Setting', {'classes': ('collapse',''), 'fields': ('description', 'article_image', 'visit_time',)
        }),
    )

    class Media:
        js = (
            '/static/kindeditor-4.1.4/kindeditor-min.js',
            '/static/kindeditor-4.1.4/lang/en.js',
            '/static/kindeditor-4.1.4/config.js'
        )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','published_date',)




# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
