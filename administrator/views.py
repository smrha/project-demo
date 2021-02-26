from django.shortcuts import render

def index(request):
    return render(request, 'administrator/apps/blog/index.html')