from django import forms
from .models import Term

class TermNewForm(forms.ModelForm):
    TERM_STATUS = (
        ('a', 'فعال'),
        ('d', 'غیرفعال')
    )

    name = forms.CharField(
        label = 'عنوان ترم',
        widget = forms.TextInput(attrs = {
            'class': 'form-control'
        }))

    begin_date = forms.DateField(
        label ='تاریخ آغاز ترم',
        widget = forms.DateInput(attrs = {
            'class': 'form-control',
            'type': 'hidden',
        }))
    
    end_date = forms.DateField(
        label ='تاریخ پایان ترم',
        widget = forms.DateInput(attrs = {
            'class': 'form-control',
            'type': 'hidden',
        }))

    status = forms.ChoiceField(
        choices = TERM_STATUS,
        label = 'وضعیت',
        widget = forms.Select(attrs = {
            'class': 'form-control'
        }))

    class Meta:
        model = Term
        fields = ['name', 'begin_date', 'end_date', 'status']