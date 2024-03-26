# views.py
from django.shortcuts import render, redirect
from home.forms import AppointmentForm
from home.models import Doctor

def home(request):
    doctors = Doctor.objects.filter(status=0)
    form = AppointmentForm()  # Instantiate the form
    return render(request, "index.html", {'doctors': doctors, 'form': form})

def addnew(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    return render(request, "index.html", {'form': form})

def about(request):
    return render(request,"about.html")
