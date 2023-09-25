from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


def home(request):
    return render(request,'home.html')

def signup(request):
    data=User.objects.all()
    return render(request,'home.html')

def signup_detail(request):
    UserName=(request.POST['username'])
    Email=(request.POST['email'])
    Password=make_password(request.POST['password'])
    lower_email=Email.lower()
    print("Email value: ",Email)

    data={
        "UserName":UserName,
        "Email":lower_email,
        "Password":Password,
    }

    a=User(UserName=UserName,Email=lower_email,Password=Password)

    if User.objects.filter(Email=lower_email).exists():

        messages.error(request,'Email Already Exist!')
        return redirect('/')
    
    if User.objects.filter(UserName=UserName).exists():
        messages.error(request,'Username Already Exist!')
        return redirect('/')
    
    
    else:
        
        a.save()
        request.session['is_logged']=True
        request.session['UserName']=a.UserName
        request.session['Email']=a.Email
        request.session['Password']=a.Password
        request.session['UserID']=a.id

        messages.success(request,'Signup Success.')
        return render(request,'dashboard.html',{'Result':a})
        


   

def login_detail(request):
    Email=(request.POST['email'])
    Password=(request.POST['password'])
    lower_email=Email.lower()
    print("Email Login & Password:",Email,Password)
    print(Email)

    try:
        context=User.objects.get(Email=lower_email)

        if User.objects.get(Email=lower_email) and check_password(Password,context.Password):
            # print("New Email:",Email)
            # if (Password==context.Password):
    
                request.session['is_logged']=True
                request.session['UserName']=context.UserName
                request.session['Email']=context.Email
                request.session['Password']=context.Password
                request.session['UserID']=context.id
                
                return render(request,'dashboard.html',{'Result':context})
                
        else:
            messages.error(request,'Invalid Password !')
            return redirect('/')
            
    except:

        messages.error(request,'Invalid Email !')
        return redirect('/')
    
    
def logout(request):
    request.session.flush()
    return redirect('/')