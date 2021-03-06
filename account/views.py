from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserEditForm, ProfileEditForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

# Login user to the site
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                    username=cd['username'],
                    password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('administrator:dashboard')
                else:
                    messages.error(request, "کاربر غیر فعال می باشد.", "text-error")
            else:
                messages.error(request, "نام کاربری و یا رمز عبور اشتباه می باشد.", "text-danger")
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'administrator/apps/account/user-login.html', context)

# Logout from the site

def user_logout(request):
    logout(request)
    return redirect('account:user_login')

# Edit and show user profile information
@login_required
def user_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account:user_profile')
        else:
            print("Invalid")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'administrator/apps/account/user-profile.html', context)