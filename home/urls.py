from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.IndexView.as_view(),name="main"),
    path("about-us", views.AboutUsView.as_view(),name="about_us"),
    path("contact-us", views.ContactUsView.as_view(),name="contact_us"),
    path("services", views.ServiceView.as_view(),name="services"),
    path("managers/",views.ManagersView.as_view(),name="managers")
]
