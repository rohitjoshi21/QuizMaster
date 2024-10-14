from django.shortcuts import render
from django.views import View
from .forms import OrganizationSignupForm, StudentSignupForm
from django.contrib.auth import authenticate, login
from .models import StudentUser, OrganizationUser
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.urls import reverse


def homepage(request):
    return render(request,"users/homepage.html")

class CustomLoginView(auth_views.LoginView):
    template_name = 'users/loginpage.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        '''
        We need to check the type of user to determine the redirecting url.
        '''
        user = self.request.user
        try:
            user_type = StudentUser.objects.get(username=user.username).user_type
        except:
            user_type = OrganizationUser.objects.get(username=user.username).user_type
        if user_type == "organization": 
            self.next_page = "/admin"
        elif user_type == "student":  
            self.next_page = "/student"
        else:
            pass #this won't be executed
        
        return super().get_success_url()


class SignupView(View):
    def get(self,request):
        return render(request,"users/presignup.html")
    
    def post(self, request):
        user_type = request.POST['user_type']
        if user_type == "organization":
            print("walk")
            return HttpResponseRedirect(reverse("orgsignup"))
        elif user_type == "student":
            print("run")
            return HttpResponseRedirect(reverse("stdsignup"))
        
        
            

class OrgSignUpView(View):
    def get(self,request):
        oform = OrganizationSignupForm()
        return render(request,"users/signup.html",{
            "form":oform
        })

    def post(self,request):
        
        oform = OrganizationSignupForm(request.POST)

        if oform.is_valid():
            cleaned_data = oform.cleaned_data

            orgname = cleaned_data['organizationname']
            email = cleaned_data['email']
            username = cleaned_data['username']
            password = cleaned_data['password']


            user = OrganizationUser.objects.create_user(username=username,organizationname=orgname,email=email,password = password)            
            user.is_staff = True
            user.save()

            return render(request,"users/homepage.html")

        else:
            return render(request,"users/signup.html",{
                "form":oform,
            })
        
class StdSignUpView(View):
    def get(self,request):
        sform = StudentSignupForm()
        return render(request,"users/signup.html",{
            "form":sform
        })

    def post(self, request):
        sform = StudentSignupForm(request.POST)
          

        if sform.is_valid():
            cleaned_data = sform.cleaned_data

            first_name = cleaned_data['first_name']
            last_name = cleaned_data['last_name']
            email = cleaned_data['email']
            username = cleaned_data['username']
            password = cleaned_data['password']
            organization = cleaned_data['organization']
            
            user = StudentUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password = password, organization = organization)
            
            user.save()

            return render(request,"users/homepage.html")

        else:
            return render(request,"users/signup.html",{
                "form":sform,
            })
            
        
