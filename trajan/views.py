from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    context = {}
    return render(request, 'trajan/index.html', context)

def physicianHome(request, physician_id):
    context = {}
    return render(request, 'trajan/physicianHome.html', context)

def patientOverview(request, patient_id):
    return HttpResponse('Patient Overview Screen: %s' % patient_id)

def newPatientVisit(request, patient_id):
    return HttpResponse('New Patient Visit: %s' % patient_id)

def ExtractingData(request, patient_id):
    return HttpResponse('Extracting Data...')

def patientVisit(request, patient_id):
    return HttpResponse('Patient Visit: %s' % patient_id)


def physicianLogin(request, physician_id):
    #print(request.POST['physId'])
    id = request.POST['physId']
    print(id)
    return HttpResponseRedirect(reverse('trajan:physicianHome', args=(id,)))

