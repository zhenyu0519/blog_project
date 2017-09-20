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
            pass
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
            pass
    except Exception as e:
        print e
    return render(request, 'post.html', locals())

def about(request):
    return render(request, 'about.html', locals())
