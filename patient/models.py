from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    mobile   = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class Prescription(models.Model):
    description = models.CharField(max_length=200)
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE)


