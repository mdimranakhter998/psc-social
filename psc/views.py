from django.shortcuts import render,HttpResponse
from .models import Contact,SignUp 

# Create your views here.
def home(request):
    if(request.method=="POST"):
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        c=Contact()
        c.name=name
        c.email=email
        c.phone=phone
        c.save()
        return render(request,'./psc/index.html')
    else:  
        return render(request,'./psc/index.html')

# sign up views
def signup(request):
    print(request.method)
    if(request.method=='POST'):
        fnm=request.POST['fname']
        lnm=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        s=SignUp()
        s.first_name=fnm
        s.last_name=lnm
        s.email=email
        s.password=password
        s.save();
        return render(request,'./psc/signin.html')
    else:
        return render(request,'./psc/signup.html')
# signin view
def signin(request):
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['password']
        sign=SignUp.objects.filter(email=email, password=password)
        print(sign)
        if(len(sign)==1):
            return render(request,'./psc/index.html')
        else:
            print("Incorrect email or password")
            return HttpResponse("icorrect password")
    else:
        return render(request,'./psc/signin.html')
