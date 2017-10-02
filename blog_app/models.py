from django.db import models

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
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField(max_length=15000, blank=False, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    published_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    visit_time = models.PositiveIntegerField(default=0, blank=False, null=False)
    comment_number = models.PositiveIntegerField(default=0, blank=False, null=False)
    article_category = models.ForeignKey(Category, blank=False, null=False)
    article_image = models.ImageField(upload_to='post_image/%Y%m%d', max_length=2000, blank=True, null=True)

    objects = ArticleManager()
    class Meta:
        ordering=['-published_date']

    def increase_visit_time(self):
        self.visit_time+=1
        self.save(update_fields=['visit_time'])

    def __unicode__(self):
        return self.title



# Comment
class Comment(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    url = models.URLField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500, blank=False, null=False)
    published_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    article = models.ForeignKey(Article, max_length=50, blank=False, null=False)
    pid = models.ForeignKey('self',blank=True, null=True)

    class Meta:
        ordering=['-published_date']

    def __unicode__(self):
        return str(self.id)