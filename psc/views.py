from django.shortcuts import redirect, render,HttpResponse
from .models import Contact,SignUp,Profile 
import uuid
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
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

#email function
def email_verification(email,token):
    print("hi email")
    subject="Email Verification"
    message='click on this link to verify your account https://pscsocial.herokuapp.com/account_verified/token'
    from_email=settings.EMAIL_HOST_USER
    To=email
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[To,])
# sign up views
def signup(request):    
    if(request.method=='POST'):
        fnm=request.POST['fname']
        lnm=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        token=uuid.uuid4       
        s=SignUp.objects.create(first_name=fnm, last_name=lnm,email=email,password=password)    
        profile=Profile.objects.create(user=s,token=token)  
        email_verification(email,token)   
       
        return render(request,'./psc/signup.html')
    else:
        print(uuid.uuid4)        
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


#account verified views
def account_verified(request,token):
    p=Profile.objects.filter(token=token)
    if(p):
        p.is_verified=True
        return redirect(signin)
    else:
        return redirect(signup)
