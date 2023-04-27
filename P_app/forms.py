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

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =['name','age','phone','visitdate', 'Details']
        labels = {'name':'Name','age':'Age','phone':'Phone-No', 'date':'visitdate'}
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'visitdate':forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'input_formats': ['%d-%m-%YT%H:%M']}),
            'Details':forms.TextInput(attrs={'class':'form-control'}),
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
