from django.shortcuts import render

def home(request):
    return render(request, 'bridge/home.html')

# Create your views here.
