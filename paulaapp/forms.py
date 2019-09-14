from django import forms
from .models import Prospect, Visit
from django.forms import inlineformset_factory
from bootstrap_datepicker_plus import DatePickerInput


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ('prospect',)
        widgets = {
            'visit_date': forms.DateInput(format='%m/%d/%Y', attrs={
                'placeholder': 'mm/dd/yyyy'
            }),
            'visit_notes': forms.TextInput(attrs={
                'placeholder': 'Visit notes'
            })
        }
    # visit_date = forms.DateField()
    # visit_notes = forms.CharField(max_length=100)


ProspectVisitFormSet = inlineformset_factory(Prospect, Visit, form=VisitForm, can_delete=True,
                                             fields=('visit_date', 'visit_notes', 'prospect'), extra=1)
