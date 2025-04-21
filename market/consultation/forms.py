from django import forms
from .models import ConsultationRequest
from .constants import CONSULTANTS

class ConsultationRequestForm(forms.ModelForm):
    consultant = forms.ChoiceField(choices=CONSULTANTS, label='Select Consultant')

    class Meta:
        model = ConsultationRequest
        fields = ['subject', 'consultant', 'date_time', 'message']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }