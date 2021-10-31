from django.shortcuts import render
from myapp.models import login
from myapp.forms import signupform,loginform
def signup_view(request):
    f=signupform()
    if request.method=='POST':
        n=signupform(request.POST)
        if n.is_valid():
            name=n.cleaned_data['name']
            email=n.cleaned_data['email']
            password=n.cleaned_data['password']
            rpassword=n.cleaned_data['rpassword']
            if password==rpassword:
                 login.objects.create(name=name,email=email,password=password,rpassword=rpassword)
                 print('successfull')
            else:
                return render(request,'myapp/msg.html')
    return render(request,'myapp/signup.html',{'form':f})
def login_view(request):
    l=loginform()
    if request.method=='POST':
        s=loginform(request.POST)
        if s.is_valid():
            u_name=s.cleaned_data['name']
            password=s.cleaned_data['password']
            user=login.objects.get(name=u_name)
            if user.name==u_name and user.password==password:
                return render(request,'myapp/details.html',{'user':user})
    else:
        return render(request,'myapp/login.html',{'form':l})
