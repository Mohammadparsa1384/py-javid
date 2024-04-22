from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("list/", views.ListArticlesView.as_view(),name="articles"),
    path("detail/<slug:slug>", views.ArticleDetailView.as_view(),name="detail"),
    path("category/<slug:slug>",views.CategoryView.as_view(),name="category"),
    path("search/",views.SearchView.as_view(),name="search")
    
]
