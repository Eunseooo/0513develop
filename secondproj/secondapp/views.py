from django.shortcuts import render
from .models import You

# Create your views here.

def hoem(request):
    members=  You.objects.all()
    return render(request, 'hoem.html' , {'members': members})
