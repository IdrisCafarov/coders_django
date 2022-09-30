from blog.models import *

def extras(request):
    context ={}
    categories = Category.objects.all()
    context['categories'] = categories

    return context
