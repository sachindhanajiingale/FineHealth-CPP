# views.py

from django.http import HttpResponse

# def greeting(request):
#     return HttpResponse("Hello! This is a greeting from the reusable app.")

from django.shortcuts import render,redirect
from P_app.models import Patient
from django.views.generic import View

def greeting(request):
    return render(request, 'greetings.html')

def contactus(request):
    return render(request, 'contactus.html')

def AllPatient_data(request):
    data = Patient.objects.all()
    return render(request, 'AllPatientdata.html', {'data': data})



