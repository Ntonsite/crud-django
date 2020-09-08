from django.db import models
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    patientName     = models.CharField(max_length=100, default='patientName')
    address         = models.CharField(max_length=100, default='sample')
    age             = models.CharField(max_length=100, default='sample address')
    phoneNumber     = models.CharField(max_length=100, default='phoneNumber')
    email           = models.EmailField(max_length=100, null=True)
    occupation      = models.CharField(max_length=100, default='occupation')
    date_registered = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.patientName


class ClinicalInfo(models.Model):
    history                = models.CharField(max_length=300, default='someHistory')
    visualAcuity           = models.CharField(max_length=300, default='some')
    ExternalEyeExamination = models.CharField(max_length=300, default='Examination')
    functionalTest         = models.CharField(max_length=300, default='Test')
    refractionDetails      = models.CharField(max_length=300, default='Details')
    Diagnosis              = models.CharField(max_length=300, default='Diagnosis')
    patient                = models.ForeignKey(Patient, on_delete=models.CASCADE)





