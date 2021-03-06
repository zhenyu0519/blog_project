from django.conf.urls import url
from blog_app.views import index, about, article, download, search,category


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^home/$', index, name='index'),
    url(r'^about/$', about, name='about'),
    # url(r'^archive/$', archive, name='archive'),
    url(r'^category/$', category, name='category'),
    url(r'^article/$', article, name='article'),
    url(r'^file/[^/]+/$', download, name='download'),
    url(r'^search/$', search, name='search'),
]
