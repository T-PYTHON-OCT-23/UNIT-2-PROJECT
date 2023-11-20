from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import SubscriptionForm, LoginForm
import json
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request:HttpRequest):
    return render(request , "main/home.html")
def city1_view(request:HttpRequest):
    return render(request , "main/city1.html")
def city2_view(request:HttpRequest):
    return render(request , "main/city2.html")
def city3_view(request:HttpRequest):
    return render(request , "main/city3.html")
def city4_view(request:HttpRequest):
    return render(request , "main/city4.html")
def success_view(request:HttpRequest):
    return render(request , "main/success.html")
def profile_view(request:HttpRequest):
    return render(request , "main/profile.html")
data=[]
def subscribe(request):
    datalist = []
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
           

            
            if not is_email_existing(email):
               
                data1 = {
                    'email': email,
                    'password': password,
                }
                
                data.append(data1)
        
                with open('data.json', 'w+', encoding="utf-8") as file:
                   contant = json.dumps(data)
                   file.write(contant)
                    
                return redirect("main:success_view")
            else:
               
                return render(request, "main/subscribe.html", {'form': form, 'error': 'Email already exists'})

    else:
        form = SubscriptionForm()

    return render(request, "main/subscribe.html", {'form': form})

def is_email_existing(email):
    

    try:
        with open('data.json', 'r', encoding="utf-8") as file:
            contant= file.read()
            data = json.loads(contant)
            
            for user_data in data:
                if user_data['email'] == email:
                    return True
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return False
    return False
def user_login(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        with open('data.json', 'r', encoding="utf-8" ) as file:
            
            contant= file.read()
            data = json.loads(contant)
            for item in data:
                if item['email'] == email and item['password'] == password:
                    response = redirect('main:profile_view')
                    response.set_cookie('login','yes')
                    return response
      
        return render(request, 'main/login.html', {'error': 'fff'})
         
    return render(request, 'main/login.html')

def user_view(request):
    user=request.user
    return render(request, 'main/profile.html',{'user':user})
   
def user_logout(request:HttpRequest):
    
        response = redirect('main:home_view')
        response.set_cookie('login','no')
                            
        return response

