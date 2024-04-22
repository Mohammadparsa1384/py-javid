from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic import TemplateView , FormView, ListView
from .models import ContactUs , Service


from home.forms import ContactForm
from django.contrib import messages
# Create your views here.
class IndexView(TemplateView):
    template_name = "home/index.html"


class AboutUsView(TemplateView):
    template_name = "home/about_us.html"
    
class ManagersView(TemplateView):
    template_name = "home/manager.html"
    
class ContactUsView(FormView):
    template_name = "home/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home:contact_us")
    
    
    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUs.objects.create(**form_data)
        messages.success(self.request,"پیام شما با موفقیت ارسال شد")
        return super().form_valid(form)
    

class ServiceView(ListView):
    template_name = "home/services.html"
    model = Service
    context_object_name = "services"