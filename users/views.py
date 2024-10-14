from django.shortcuts import render
from django.views import View
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .models import MyUser
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect

def homepage(request):
    return render(request,"users/homepage.html")

class CustomLoginView(auth_views.LoginView):
    template_name = 'users/loginpage.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        '''
        We need to check the type of user to determine the redirecting url
        '''
        user = self.request.user
        user_type = MyUser.objects.get(username=user.username).user_type
        if user_type == "organization": 
            self.next_page = "/admin"
        elif user_type == "student":  
            self.next_page = "/dashboard"
        else:
            pass #this won't be executed
        
        return super().get_success_url()


class SignupView(View):
    def get(self,request):
        form = SignupForm()
        return render(request,"users/signup.html",{
            "form":form
        })

    def post(self,request):
        form = SignupForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            first_name = cleaned_data['first_name']
            last_name = cleaned_data['last_name']
            email = cleaned_data['email']
            username = cleaned_data['username']
            password = cleaned_data['password']
            user_type = cleaned_data['user_type']

            
            user = MyUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password = password,user_type=user_type)
            
            if user_type == "organization":
                user.is_staff = True
            user.save()

            return render(request,"users/homepage.html")

        else:
            return render(request,"users/signup.html",{
                "form":form
            })
            
        
