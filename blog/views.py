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

def sub_view(request):
    
    return render(request,"sub.html")




def category_detail(request,slug):
    context ={}

    category = get_object_or_404(Category,slug=slug)
    context['category']=category

    return render(request,"category_detail.html",context)


from .forms import PostForm

def post_form_view(request):
    print("data")
    print(request.method)
    form = PostForm()

    if request.method == "POST":
        print(request.POST)
        print(request.FILES)


        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print(instance)
        else:
            print(form.errors)

    context = {
        "form": form
    }
    return render(request, "form.html", context)