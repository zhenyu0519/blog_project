from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',locals())

def home(request):
    return render(request,'index.html',locals())

def post(request):
    return render(request, 'post.html', locals())

def about(request):
    return render(request, 'about.html', locals())
