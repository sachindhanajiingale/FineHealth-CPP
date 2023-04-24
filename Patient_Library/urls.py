# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    # path('contactus/', views.contactus, name='contactus'),
    path('AllPatient_data/', views.AllPatient_data, name='AllPatient_data'),


]
