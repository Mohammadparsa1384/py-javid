from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60,verbose_name="عنوان")    
    created = models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    updated = models.DateTimeField(auto_now=True,verbose_name="زمان آپدیت")
    slug = models.SlugField(blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"slug": self.slug})
    

    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = " دسته بندی ها"
    
    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=60,verbose_name="عنوان")
    category = models.ManyToManyField(Category , related_name="articles",verbose_name="دسته بندی")
    
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="articles",verbose_name="نویسنده")
    created = models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    updated = models.DateTimeField(auto_now=True,verbose_name="زمان آپدیت")
    body = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="articles", null=True, blank=True,verbose_name="عکس وبلاگ")
    slug = models.SlugField(null=True , blank=True)
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ("-created","-updated")
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name="comments",verbose_name="مقاله")
    body = models.TextField(verbose_name="دیدگاه")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments",verbose_name="کاربر")    
    parent = models.ForeignKey("self",on_delete=models.CASCADE, related_name="replies",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ارسال")    
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"
    
    def __str__(self) -> str:
        return self.body[:30]    