from . import views
from django.urls import path

app_name = "accounts"
# root = account
urlpatterns = [
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("register/",views.UserRegisterView.as_view(),name="register"),
    path("logout/",views.UserLogoutView.as_view(),name="logout"),
]
