from django.shortcuts import redirect, render

from django.contrib.auth import login , logout , authenticate

from django.contrib.auth.models import User

from django.views import View

from .forms import LoginForm, RegisterForm
# Create your views here.

class UserLoginView(View):
    
    def get(self,request):
        if self.request.user.is_authenticated:
            return redirect("/")
        form = LoginForm()
        return render(self.request,"accounts/login.html",{'form':form})
    
    
    def post(self,request):
        form = LoginForm(data=self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(self.request,username=username,password=password)
            if user is not None:
                login(self.request, user)
                return redirect("home:main")
            else:
                form.add_error("username","اطلاعات وارد شده نادرست است")
                
        return render(self.request,"accounts/login.html",{'form':form})
            
class UserRegisterView(View):
    
    def get(self,request):
        form = RegisterForm()
        return render(self.request,"accounts/register.html",{'form':form})
    
    def post(self,request):
        form = RegisterForm(data=self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create(username=username,password=password)
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect("/")
            
        return render(self.request,"accounts/register.html",{'form':form})


class UserLogoutView(View):
    
    def get(self,request):
        logout(request)
        return redirect("/")
        