from django.shortcuts import render
from aiservice.models import AI
# Create your views here.

def about(request):
    return render(request, "about.html")

def index(request):
    
    ai_objects = AI.objects.all()
    return render(request, "index.html",{'ai_objects': ai_objects})


