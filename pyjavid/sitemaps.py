from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Article

class StaticViewSiteMap(Sitemap):
    def items(self):
        return ["home:main",
                "home:about_us",
                "home:contact_us",
                "home:services",
                "home:managers",
                ]
    
    def location(self,item):
        return reverse(item)

class ArticleViewSitemap(Sitemap):
    def items(self):
        return Article.objects.all()