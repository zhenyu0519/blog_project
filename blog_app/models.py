from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Category
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    index_order = models.IntegerField(default=999)

    def __unicode__(self):
        return self.category_name

# Article Manager
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('published_date')
        for date in date_list:
            date = date['published_date'].strftime('%Y-%m Archives')
            # print date
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

# Article
class Article(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=250)
    content = RichTextField(max_length=60000)
    author = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)
    visit_time = models.PositiveIntegerField(default=0)
    article_category = models.ForeignKey(Category)
    article_image = models.ImageField(upload_to='%Y%m%d', max_length=3000)

    objects = ArticleManager()
    class Meta:
        ordering=['-published_date']

    def increase_visit_time(self):
        self.visit_time+=1
        self.save(update_fields=['visit_time'])

    def __unicode__(self):
        return self.title

