from django.shortcuts import render
from django.views import View
from .forms import OrganizationSignupForm, StudentSignupForm
from django.contrib.auth import authenticate, login
from .models import StudentUser, OrganizationUser
from dashboard.models import Quiz, Question
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType



class CustomLoginView(auth_views.LoginView):
    template_name = 'users/loginpage.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        '''
        We need to check the type of user to determine the redirecting url.
        '''
        user = self.request.user
        if user.is_superuser or user.is_staff:
            self.next_page = "/organization"
        else:  
            self.next_page = "/student"
        
        return super().get_success_url()


class SignupView(View):
    def get(self,request):
        return render(request,"users/presignup.html")
    
    def post(self, request):
        user_type = request.POST['user_type']
        if user_type == "organization":
            return HttpResponseRedirect(reverse("orgsignup"))
        elif user_type == "student":
            return HttpResponseRedirect(reverse("stdsignup"))
        
        
            

class OrgSignUpView(View):
    def get(self,request):
        oform = OrganizationSignupForm()
        return render(request,"users/signup.html",{
            "form":oform,
            "user_type":"organization"
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

            group = Group.objects.get(name='organization_admin')
            user.groups.add(group)

            user.save()

            login(request,user)
            return HttpResponseRedirect(reverse("login"))

        else:
            return render(request,"users/signup.html",{
                "form":oform,
            })
        
class StdSignUpView(View):
    def get(self,request):
        sform = StudentSignupForm()
        return render(request,"users/signup.html",{
            "form":sform,
            "user_type":"organization"
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

            login(request,user)

            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request,"users/signup.html",{
                "form":sform,
            })
            
        
