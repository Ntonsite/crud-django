from django import forms
from .models import Patient, Prescription

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'



class PrecriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrecriptionForm, self).__init__(*args, **kwargs)
        self.fields['patient'].empty_label = "select"