from django.shortcuts import render

# Protection Secure Auth (direct URLs)
from django.contrib.auth.decorators import login_required
# Protection Secure URLs (history)
from django.views.decorators.cache import cache_control 

from App.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

# Function to render frontend
def frontend(request):
    return render(request, "frontend.html")

# -------------  Backend Section  ----------------
# Function to render backend
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter (
            Q(firstname__icontains=q) | Q(lastname__icontains=q) | Q(email__icontains=q) | Q(age__icontains=q) | Q(gender__icontains=q) | Q(note__icontains=q)
        ).order_by('-created_at')   
    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')
    paginator = Paginator(all_patient_list, 5)
    page = request.GET.get('page')
    filtered_patients = paginator.get_page(page)

    return render(request, "backend.html", {"patients":filtered_patients,"all_patients":all_patient_list})

# @login_required(login_url="login")
# def backend(request):
#     return render(request, "backend.html")
    
# Function to insert new patient
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def add_patient(request):
    if request.method == 'POST':
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
            messages.success(request, "Patient Added successfully!")
            return HttpResponseRedirect('/backend')
        else:
            messages.error(request, "Failed!")
            return HttpResponseRedirect('/backend')
    else:
        return render(request, "backend.html")

# Update Patient
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def update_patient(request, patient_id):
    if request.method == 'POST':
        patient = Patient.objects.get(id = patient_id)
        if patient != None:
            patient.firstname = request.POST.get('firstname')
            patient.lastname = request.POST.get('lastname')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient Updated successfully!")
            return HttpResponseRedirect('/backend')
        else:
            messages.error(request, "Failed!")
            return HttpResponseRedirect('/backend')

# Delete Patient
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    patient.delete()

    messages.success(request, "Patient Deleted successfully!")
    return HttpResponseRedirect('/backend')


# PATIENTS' ACCESS HERE
# @login_required(login_url="login")
# def patient(request, patient_id):
#     patient = Patient.objects.get(id = patient_id)
#     if patient != None:
#         return render(request, "edit.html", {patient:'patient'})
