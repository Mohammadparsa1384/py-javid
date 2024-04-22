from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render , get_object_or_404
from django.core.paginator  import Paginator

from django.views.generic import ListView , View , DetailView

from .models import Article, Category, Comment
# Create your views here.

class ListArticlesView(ListView):
    template_name = "blog/list_articles.html"
    context_object_name = "articles"
    queryset = Article.objects.all()
    paginate_by = 2
    
    
class ArticleDetailView(DetailView):
        model = Article
        
        
        
        def post(self,request,slug):
            
            parent_id = self.request.POST.get("parent_id")
            body = self.request.POST.get("body")
            Comment.objects.create(article=self.get_object(),user=self.request.user,body=body,parent_id=parent_id)
            
            return render(self.request,"blog/article_detail.html",{"article":self.get_object()})
            

class CategoryView(View):
    def get(self,request,slug):
        cat = get_object_or_404(Category,slug=slug)
        list_articles = cat.articles.all()
        return render(self.request,'blog/list_articles.html',{"articles":list_articles})
        
class SearchView(ListView):
    
    def get(self,request):
        q = request.GET.get("q")
        articles = Article.objects.filter(title__icontains=q)
        return render(request,"blog/list_articles.html",{"articles":articles})
        

        
    