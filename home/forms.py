from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    
    class Meta:
        model =  ContactUs
        fields = "__all__"
        
        widgets = {
            "subject": forms.TextInput({"class":"form-control","placeholder":"موضوع"}),
            "desc": forms.Textarea({"class":"form-control","placeholder":"توضیحات"}),
        } 