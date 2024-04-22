from django.db import models

# Create your models here.
class ContactUs(models.Model):
    subject = models.CharField(max_length=40)
    desc = models.TextField()
    
    class Meta:
        verbose_name = "تماس "
        verbose_name_plural = "تماس ها"
        
    def __str__(self) -> str:
        return self.subject
    

class Service(models.Model):
    title = models.CharField(max_length=30,verbose_name = "عنوان سرویس")
    description = models.TextField(verbose_name= "توضیحات")
    image = models.ImageField(verbose_name="عکس",upload_to="services")
    
    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "سرویس ها"
    
    def __str__(self) -> str:
        return self.title
    