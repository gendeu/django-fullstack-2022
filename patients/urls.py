"""patients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Native path
    path('admin/', admin.site.urls),
    # Path to Frontend
    path('', views.frontend, name="frontend"),
    
    # Path to Login / Logout
    path("login/", include('django.contrib.auth.urls')),
    
    # -------------  Backend Section  ----------------
    # Path to Backend
    path('backend/', views.backend, name="backend"),

    # Path to Add Patient
    path('add_patient', views.add_patient, name="add_patient"),
    # Path to Edit Patient
    path('update_patient/<str:patient_id>', views.update_patient, name="update_patient"),
    # Path to Delete Patient
    path('delete_patient/<str:patient_id>', views.delete_patient, name="delete_patient"),
]
