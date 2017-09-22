from django.shortcuts import render
from models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    try:
        category_list = Category.objects.all()
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 3)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)

        archive_list = Article.objects.distinct_date()
        # for a in archive_list:
        #     print a
    except Exception as e:
        print e
    return render(request,'index.html',locals())

def home(request):
    return render(request,'index.html',locals())

def post(request):
    try:
        category_list = Category.objects.all()
        article_list = Article.objects.all()
        paginator = Paginator(article_list,5)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            article_list=paginator.page(1)
        archive_list = Article.objects.distinct_date()
    except Exception as e:
        print e
    return render(request, 'post.html', locals())

def article(request):
    id = request.GET.get('id', None)
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return render(request,'failure.html',{'reason':'No matched article found'})

    return render(request, 'article.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def archive(request):
    try:
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        article_list = Article.objects.filter(published_date__icontains=year+'-'+month)
        paginator = Paginator(article_list, 5)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
        archive_list = Article.objects.distinct_date()
    except Exception as e:
        pass
    return render(request,'archive.html',locals())
