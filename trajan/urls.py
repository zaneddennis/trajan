from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('physician/<int:physician_id>/',
         views.physicianHome, name='physicianHome'),

    path('patients/<int:patient_id>/',
         views.patientOverview, name='patientOverview'),

    path('patients/<int:patient_id>/newVisit',
         views.newPatientVisit, name='newPatientVisit'),

    path('patients/<int:patient_id>/extracting',
         views.ExtractingData, name='extractingData'),

    path('patients/<int:patient_id>/visit',
         views.patientVisit, name='patientVisit')
]