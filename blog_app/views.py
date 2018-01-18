from django.shortcuts import render
from models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.http import HttpResponse
import os


# Create your views here.
def index(request):
    try:
        category_list = Category.objects.all()
        article_list = Article.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(article_list, 5)
        try:
            article_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)

        # archive_list = Article.objects.distinct_date()
        # for a in archive_list:
        #     print a
    except Exception as e:
        print e
    return render(request, 'index.html', locals())


def home(request):
    return render(request, 'index.html', locals())


def article(request):
    id = request.GET.get('id', None)
    try:
        article = Article.objects.get(pk=id)
        article.increase_visit_time()
        article.save()
    except Article.DoesNotExist:
        return render(request, 'error.html', {'reason': 'No matched article found'})

    return render(request, 'article.html', locals())



def about(request):
    return render(request, 'about.html', locals())


# def archive(request):
#     try:
#         year = request.GET.get('year', None)
#         month = request.GET.get('month', None)
#         article_list = Article.objects.filter(published_date__icontains=year + '-' + month)
#         paginator = Paginator(article_list, 5)
#         try:
#             page = int(request.GET.get('page', 1))
#             article_list = paginator.page(page)
#         except(EmptyPage, InvalidPage, PageNotAnInteger):
#             article_list = paginator.page(1)
#         archive_list = Article.objects.distinct_date()
#     except Exception as e:
#         pass
#     return render(request, 'archive.html', locals())


def download(request):
    def read_file(fn, buf_size=262166):
        f = open(fn, 'rb')
        while True:
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/file/resume.pdf'
    response = HttpResponse(read_file(path), content_type='APPLICATION/OCTET=STREAM')
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'
    response['Content-Length'] = os.path.getsize(os.path.join(path))
    return response


def search(request):
    keyword = request.GET.get('keyword', None)
    error_msg = ""

    if not keyword:
        error_msg = "Please enter keyword"
        return render(request, 'search_result.html', {'error_msg': error_msg})

    try:
        category_list = Category.objects.all()
        # article_list = Article.objects.all()
        article_list = Article.objects.filter(title__icontains=keyword, content__icontains=keyword)
        paginator = Paginator(article_list, 5)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
        # archive_list = Article.objects.distinct_date()
    except Exception as e:
        print(e)
    return render(request, 'search_result.html', locals())

def category(request):
    try:
        category_list = Category.objects.all()
        category=request.GET.get('category', None)
        article_list = Article.objects.filter(article_category__category_name__icontains=category)
        paginator = Paginator(article_list, 5)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        pass
    return render(request, 'category_result.html', locals())
