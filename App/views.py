from django.shortcuts import render

# My Imports
from django.contrib.auth.decorators import login_required
from App.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect

# Function to render frontend
def frontend(request):
    return render(request, "frontend.html")

# -------------  Backend Section  ----------------
# Function to render frontend
@login_required(login_url="login")
def backend(request):
    return render(request, "backend.html")

# Function to insert new patient
@login_required(login_url="login")
def add_patient(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            patient = Patient()
            patient.firstname = request.POST.get('firstname')
            patient.lastname = request.POST.get('lastname')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient added successfully!")
            return HttpResponseRedirect('/backend')
        # else:
        #     messages.error(request, "Failed!")
            # return HttpResponseRedirect('/backend')
    else:
        return render(request, "add_patient.html")