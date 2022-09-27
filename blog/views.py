from unicodedata import category
from django.shortcuts import render,get_object_or_404
from blog.models import Post,Category
# Create your views here.


def index_view(request):
    xeberler = Post.objects.filter(draft=True)
    news_count = Post.objects.all().count()
    
    kateqoriyalar = Category.objects.all
    latests = Post.objects.order_by('-created_date')
    
    context = {
        "xeberler":xeberler,
        "kateqoriyalar":kateqoriyalar,
        "latests":latests,
        "news_count":news_count
    }
    return render(request,"index.html",context)


def detail_news(request,slug):
    context={}
    xeber = get_object_or_404(Post,slug=slug)
    context['other_news']=Post.objects.filter(draft=True).exclude(pk=xeber.id)
    context['xeber']=xeber

    return render(request,"detail.html",context)
