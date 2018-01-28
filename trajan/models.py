from django.db import models

class Patient(models.Model):
    patient_name = models.CharField(max_length=32)
    patient_age = models.IntegerField(default=-1)
    patient_birthdate = models.CharField(max_length=10)

    def __str__(self):
        return self.patient_name

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_dateTime = models.DateTimeField('visit date')

    visit_chiefComplaint = models.CharField(max_length=256)
    visit_complaintDuration = models.CharField(max_length=64)
    visit_complaintFrequency = models.CharField(max_length=64)
    visit_complaintQuality = models.CharField(max_length=128)
    visit_complaintSymptoms = models.CharField(max_length=512)
    visit_complaintLocation = models.CharField(max_length=64)
    visit_aggravatingFactors = models.CharField(max_length=256)
    visit_alleviatingFactors = models.CharField(max_length=256)

    def __str__(self):
        return str(self.patient) + ' ' + str(self.visit_dateTime)

