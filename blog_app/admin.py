from django.contrib import admin
from models import *


# Set up the models in admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'article_category', 'published_date',)

    list_filter = ('title','article_category', 'published_date',)


    fieldsets = (
        (None, {'fields': ('title', 'content', 'author', 'article_category')}),
        ('Advanced Setting', {'classes': ('collapse',''), 'fields': ('description', 'article_image',)
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)



# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
