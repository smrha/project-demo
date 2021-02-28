from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserEditForm, ProfileEditForm

def login(request):
    return render(request, 'account/login.html')

# Edit and show user profile information
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