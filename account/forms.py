from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label = 'نام کاربری',
        widget = forms.TextInput(attrs = {
            'class': 'form-control'
        }))

    password = forms.CharField(
        label = 'رمز عبور',
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control'
        }))

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        label ='نام',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': ''
        }))

    last_name = forms.CharField(
        label ='نام خانوادگی',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': ''
        }))

    email = forms.EmailField(
        label ='ایمیل',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': ''
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    mobile = forms.CharField(
        label ='تلفن همراه',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': ''
        }))

    address = forms.CharField(
        label ='آدرس',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': ''
        }))

    birthday = forms.DateField(
        label ='تاریخ تولد',
        widget = forms.DateInput(attrs = {
            'class': 'form-control',
            'placeholder': ''
        }))

    class Meta:
        model = Profile
        fields = ['mobile', 'address', 'birthday']