from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient

# Create your views here.

def patient_list(request):
    context = {'patient_list': Patient.objects.all()}

    return render(request, "patient/patient_list.html",context)


def patient_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)

        return render(request, "patient/patient_form.html", {'form':form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()

        return redirect('/patient/list')
        


def patient_delete(request, id):
    patient = Patient.objects.get(pk=id)
    patient.delete()


    return redirect('/patient/list')