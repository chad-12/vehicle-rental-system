from django.shortcuts import render
from .models import Vehicle

def home(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'home.html', {'vehicles': vehicles})