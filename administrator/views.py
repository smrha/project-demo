from django.shortcuts import render

def dashboard(request):
    return render(request, 'administrator/apps/dashboard.html')