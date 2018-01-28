from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .extraction import *

def index(request):
    context = {}
    return render(request, 'trajan/index.html', context)

def physicianHome(request, physician_id):
    context = {}
    return render(request, 'trajan/physicianHome.html', context)

def patientOverview(request, patient_id):
    context = {}
    return render(request, 'trajan/patientOverview.html', context)

def newPatientVisit(request, patient_id):
    context = {}
    return render(request, 'trajan/newVisit.html', context)

def extractingData(request, patient_id):
    extractFields("Hello World")
    return HttpResponse('Extracting Data...')

def patientVisit(request, patient_id):
    context = {}
    return render(request, 'trajan/visit.html', context)


def physicianLogin(request, physician_id):
    #print(request.POST['physId'])
    id = request.POST['physId']
    print(id)
    return HttpResponseRedirect(reverse('trajan:physicianHome', args=(id,)))
