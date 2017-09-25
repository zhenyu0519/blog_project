from django.conf.urls import url
from blog_app.views import index, post, about, archive, article, comment_post,download

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^home/$', index, name='index'),
    url(r'^post/$', post, name='post'),
    url(r'^about/$', about, name='about'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^article/$', article, name='article'),
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^file/[^/]+/$', download, name='download'),
]
