import email

from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import CreateView, TemplateView
from amdin1.models import Profile
from .forms import SignUpForm, UserForm, ProfileForm

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(req):
    return render(req,'common/home.html')

class SignUpView(CreateView):
    form_class = SignUpForm
    # subject = 'WELCOME'
    # print()
    # html_message = render_to_string('common/mail.html', {'name':SignUpForm})
    # plain_message = strip_tags(html_message)
    # from_email = 'manshu.work@gmail.com'
    # to = email
    # #
    # mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'
def register(req):
    return render(req, 'common/register.html')


def DashboardView(req):
    return render(req, 'common/dashboard.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



# def login_data(req):
#     return render(req,'amdin1/login.html')
#
#
#
#
#
#
#
# def signup_user(req):
#     if req.method == "POST":
#         username = req.POST['username']
#         Name = req.POST['name']
#         email = req.POST['email']
#         mobile = req.POST['number']
#         password = req.POST['pass']
#         repassword = req.POST['repeatpassword']
#         if password != repassword:
#             return HttpResponse("password not match")
#         if User.objects.filter(username=username).exists():
#
#             return HttpResponse("user alredy exist")
#         else:
#             data = Admin_register(username=username, name=Name, email=email, password=password,mobile_number=mobile)
#             myuser = User.objects.create_user(username=username,email= email, password=password ,first_name=Name)
#             data.save()
#             myuser.save()
#
#
#             subject = 'WELCOME'
#             html_message = render_to_string('amdin1/mail.html', {'name': Name,'username':username,'password':password,'email':email,'number':mobile})
#             plain_message = strip_tags(html_message)
#             from_email = 'manshu.work@gmail.com'
#             to = email
#
#             mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
#             return render(req,'amdin1/login.html')
#
#
#
#
# def user_login(req):
#     if req.method == "POST":
#         user_name = req.POST['username']
#         user_pass = req.POST['password']
#         auth_user = authenticate(username=user_name, password=user_pass)
#
#         logind = Login_data(req, auth_user)
#         print(logind)
#         return render(req,'amdin1/index.html')
#
# def addcustmer(req):
#     return render(req,'amdin1/add-customer.html')