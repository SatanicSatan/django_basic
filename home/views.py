from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent!!!!!!!!!!!!!"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage??")

# def index(request):
#     return HttpResponse("this is INDEX^^^^^^^^^")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is About!!!!")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services@@@@@")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.!')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact########")

def handelSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input

        #username under 10 chrs
        if len(username) > 10:
            messages.error(request, "not more then 10 chrs")
            return redirect('home')

        #username alphanumeric
        if not username.isalnum():
            messages.error(request, "letters and number must")
            return redirect('home')

        #password match
        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')


        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your sami Account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


def handelLogin(request):
        if request.method == "POST":
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']

            user = authenticate(username=loginusername,
            password=loginpassword)

            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect('home')
            else:
                messages.success(request, "Invalid Credentials, try again")
                return redirect('home')
        return HttpResponse('handelLogin')



def handelLogout(request):
    return HttpResponse('handelLogout')