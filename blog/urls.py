from django.urls import path
from blog.views import *


app_name ="blog"

urlpatterns = [
    path('',index_view,name="index"),
    path('xeber/<slug>/',detail_news,name="detail_news"),
    path('sub',sub_view,name="sub"),
    path('category_detail/<slug>/',category_detail,name="category_detail")
]
