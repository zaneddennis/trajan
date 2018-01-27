from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'trajan/index.html', context)

def physicianHome(request, physician_id):
    context = {}
    return render(request, 'trajan/TAMUHack/physicianHome.html', context)

def patientOverview(request, patient_id):
    return HttpResponse('Patient Overview Screen: %s' % patient_id)

def newPatientVisit(request, patient_id):
    return HttpResponse('New Patient Visit: %s' % patient_id)

def ExtractingData(request, patient_id):
    return HttpResponse('Extracting Data...')

def patientVisit(request, patient_id):
    return HttpResponse('Patient Visit: %s' % patient_id)

