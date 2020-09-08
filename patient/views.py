from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import PatientForm
from .models import Patient

# Create your views here.


class PatientListView(ListView):
    model = Patient
    template_name = 'patient/patient_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'patient_list'
    paginate_by = 5
    queryset = Patient.objects.all()



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