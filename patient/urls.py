from django.urls import path
from . import views
from . views import PatientListView

urlpatterns = [
    path('', views.patient_form, name='patient_insert'), #get and post for insert operation
    path('<int:id>/', views.patient_form, name='patient_update'), #get and post for update
    path('delete/<int:id>/', views.patient_delete, name='patient_delete'), #get and post for update
    path('list/', PatientListView.as_view(), name='patient_list'), #get request and display all records
]
