from django import forms
class signupform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
class loginform(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
