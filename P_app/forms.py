from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from . models import Patient

# class AddPatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields =['name','age','phone','Details']
#         lables = {'name':'Name','age':'Age','phone':'Phone-No'}
#         widgets ={
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'age':forms.NumberInput(attrs={'class':'form-control'}),
#             'phone':forms.TextInput(attrs={'class':'form-control'}),
#             'Details':forms.TextInput(attrs={'class':'form-control'}),
#         }

DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S','%Y-%m-%d %I:%M:%S %p','%Y-%m-%d %I:%M %p','%Y-%m-%d %H:%M','%Y-%m-%d','%m/%d/%Y %H:%M:%S', '%m/%d/%Y %I:%M:%S %p', '%m/%d/%Y %I:%M %p', '%m/%d/%Y %H:%M', '%m/%d/%Y']

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'phone', 'Details', 'visitdate']
        labels = {'name': 'Name', 'age': 'Age', 'phone': 'Phone-No', 'visitdate': 'Visit Date and Time'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Details': forms.TextInput(attrs={'class': 'form-control'}),
            'visitdate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'input_formats': DATETIME_INPUT_FORMATS}),
        }
        
class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password = forms.CharField(
        label= "Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )
    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }
