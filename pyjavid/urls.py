"""
URL configuration for pyjavid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include


from . import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from .sitemaps import StaticViewSiteMap , ArticleViewSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {"static": StaticViewSiteMap, "articles":ArticleViewSitemap}

urlpatterns = [
    
    path('robots.txt',TemplateView.as_view(template_name="robots.txt",content_type="text/plain")),
    path("sitemap.xml", sitemap, {"sitemaps":sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('account/', include('accounts.urls')),
    path("articles/", include("blog.urls"))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
