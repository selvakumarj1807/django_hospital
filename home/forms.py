# forms.py
from django import forms
from home.models import Appoitment, Doctor

class AppointmentForm(forms.ModelForm):
    select_doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Choose Doctor", widget=forms.Select(attrs={'class': 'form-select border-0', 'style': 'height: 55px;'}))
    
    class Meta:
        model = Appoitment
        fields = ['name', 'contact', 'email', 'date', 'time', 'select_doctor', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0', 'placeholder': 'Your Name', 'style': 'height: 55px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-0', 'placeholder': 'Your Email', 'style': 'height: 55px;'}),
            'contact': forms.TextInput(attrs={'class': 'form-control border-0', 'placeholder': 'Your Mobile', 'style': 'height: 55px;'}),
            'date': forms.TextInput(attrs={'class': 'form-control border-0 datetimepicker-input', 'placeholder': 'Choose Date', 'style': 'height: 55px;', 'data-target': '#date', 'data-toggle': 'datetimepicker'}),
            'time': forms.TextInput(attrs={'class': 'form-control border-0 datetimepicker-input', 'placeholder': 'Choose Time', 'style': 'height: 55px;', 'data-target': '#time', 'data-toggle': 'datetimepicker'}),
            'description': forms.Textarea(attrs={'class': 'form-control border-0', 'placeholder': 'Describe your problem', 'rows': '5'}),
        }
