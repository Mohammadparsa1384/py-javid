from blog.models import Article, Category

def show_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}

def recent_articles(request):
    articles = Article.objects.order_by("-created","-updated")[:3]
    return {"recent_articles":articles}