from django import forms
from django.utils.translation import gettext_lazy as _
from .models.employees import Employee
from .enum import WeekDaysEnum


class MultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = WeekDaysEnum.choices()
        kwargs['widget'] = forms.CheckboxSelectMultiple()
        super().__init__(*args, **kwargs)


class EmployeeAdminForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance
