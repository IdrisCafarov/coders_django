from django.urls import path
from blog.views import *


urlpatterns = [
    path('',index_view,name="index"),
    path('xeber/<slug>/',detail_news,name="detail_news")
]
