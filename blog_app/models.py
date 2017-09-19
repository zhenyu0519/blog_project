from django.db import models

# Create your models here.

# Category
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    index_order = models.IntegerField(default=999)

    def __unicode__(self):
        return self.category_name

# Article
class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField(max_length=10000, blank=False, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    published_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    visit_time = models.IntegerField(blank=False, null=False)
    article_category = models.ForeignKey(Category, blank=False, null=False)
    article_image = models.ImageField(upload_to='post_image/%Y%m%d', max_length=2000, blank=True, null=True)

    class Meta:
        ordering=['-published_date']

    def __unicode__(self):
        return self.title



# Comment
class Comment(models.Model):
    content = models.CharField(max_length=500, blank=False, null=False)
    published_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    article = models.ForeignKey(Article, max_length=50, blank=False, null=False)

    class Meta:
        ordering=['-published_date']

    def __unicode__(self):
        return str(self.id)