from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render

def main(request):
    return render(request, 'Portfolio/main.html')
# def home(request):
#     return render(request, 'Portfolio/home.html')
def about_me(request):
    return render(request, 'Portfolio/about_me.html')
def projects(request):
    return render(request, 'Portfolio/projects.html')

def contact_me(request):
    return render(request, 'Portfolio/contact_me.html')
