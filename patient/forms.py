from django import forms
from .models import Patient, ClinicalInfo

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'



class ClinicalInfoForm(forms.ModelForm):

    class Meta:
        model = ClinicalInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClinicalInfoForm, self).__init__(*args, **kwargs)
        self.fields['patient'].empty_label = "select"