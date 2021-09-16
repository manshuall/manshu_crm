"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from amdin1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from amdin1.views import SignUpView, ProfileUpdateView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home ,name='home'),
    path('', views.home),
    path('dashboard', views.DashboardView ,name='dashboard'),

    # Authentication
    path('register/', SignUpView.as_view(), name="register"),

    path('login/', auth_views.LoginView.as_view(template_name='common/login.html', success_url='dashboard'),name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),
path('password-reset/',auth_views.PasswordResetView.as_view(
                           template_name='common/password-reset/password_reset.html',
                           subject_template_name='common/password-reset/password_reset_subject.txt',
                           email_template_name='common/password-reset/password_reset_email.html',
                           # success_url='/login/'
                       ),
                       name='password_reset'),
path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
                           template_name='common/password-reset/password_reset_done.html'
                       ),
                       name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
                           template_name='common/password-reset/password_reset_confirm.html'
                       ),
                       name='password_reset_confirm'),
path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(
                           template_name='common/password-reset/password_reset_complete.html'
                       ),
                       name='password_reset_complete'),

path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
path('profile/', ProfileView.as_view(), name='profile'),

                  # path('register.html', views.register),
    # path('login.html', views.login_data),
    # path('signup', views.signup_user),
    # path('login_user', views.user_login),
    # path('add_custmer', views.addcustmer),
    #
    # path('reset_password/',
    #      auth_views.PasswordResetView.as_view(template_name="amdin1/password_reset.html"),
    #      name="reset_password"),
    #
    # path('reset_password_sent/',
    #      auth_views.PasswordResetDoneView.as_view(template_name="amdin1/password_reset_sent.html"),
    #      name="password_reset_done"),
    #
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name="amdin1/password_reset_form.html"),
    #      name="password_reset_confirm"),
    #
    # path('reset_password_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name="amdin1/password_reset_done.html"),
    #      name="password_reset_complete"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


