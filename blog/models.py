from enum import unique
from wsgiref.validate import validator
from django.db import models
from blog.helper import seo
from django.urls import reverse
from .validators import validate_title

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name="Kateqoriya adi")
    slug = models.SlugField(unique=True,editable=False,null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = seo(self.title + "-" + str(self.id))
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'slug': self.slug})
    

class SubCategory(models.Model):
    title = models.CharField(max_length=50,verbose_name="Sub Kateqoriya")
    category = models.ForeignKey(Category,related_name="category_sub",on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,editable=False,null=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SubCategory, self).save(*args, **kwargs)
        self.slug = seo(self.title + "-" + str(self.id))
        super(SubCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:event_detail', kwargs={'slug': self.slug})
    
    


class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name="Basliq", validators=[validate_title])
    content = models.TextField(verbose_name="Xeber")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True,verbose_name="publish")
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,related_name="post_category")
    image = models.ImageField(upload_to="post_img",null = True)
    slug = models.SlugField(null=True,unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xeber"
        verbose_name_plural = "Xeberler"
        ordering=["-id"]
    
    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super(Post, self).save(*args, **kwargs)
    
    