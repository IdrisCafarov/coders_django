
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name="Kateqoriya adi")

    def __str__(self):
        return self.title
    


class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name="Basliq")
    content = models.TextField(verbose_name="Xeber")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True,verbose_name="publish")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name="post_category")
    image = models.ImageField(upload_to="post_img",null = True)
    slug = models.SlugField(null=True,unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xeber"
        verbose_name_plural = "Xeberler"

    
    