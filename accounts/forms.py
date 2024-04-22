from django import forms

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core import validators
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput({"class":"form-control","placeholder":"نام کاربری"}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput({"class":"form-control","placeholder":"رمز عبور"}))    
    
class RegisterForm(forms.Form):
        username = forms.CharField(max_length=30,widget=forms.TextInput({"class":"form-control","placeholder":"نام کاربری"}))
        password = forms.CharField(max_length=30,validators=[validators.MinLengthValidator(5)],widget=forms.PasswordInput({"class":"form-control","placeholder":"رمز عبور"}))
        password2 = forms.CharField(max_length=30,validators=[validators.MinLengthValidator(5)],widget=forms.PasswordInput({"class":"form-control","placeholder":"تکرار رمز عبور "}))

        def clean(self) :
            cd =  super().clean()
            password = self.cleaned_data.get("password")
            password2 = self.cleaned_data.get("password2")
            if password != password2:
                raise ValidationError("پسورد ها مشابه نیستند")  
            return cd
        
        def clean_username(self):
            username = self.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                raise ValidationError("این نام کاربری قبلا انتخاب شده است یک نام کاربری جدید وارد کنید")
            return username
        
          
            
              