from django.shortcuts import render

# My Imports
from django.contrib.auth.decorators import login_required

# Function to render frontend
def frontend(request):
    return render(request, "frontend.html")

# -------------  Backend Section  ----------------
# Function to render frontend
@login_required(login_url="login")
def backend(request):
    return render(request, "backend.html")
