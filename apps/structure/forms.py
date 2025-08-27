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
    admission_days_choices = MultipleChoiceField(
        label=_("Qabul kunlari"),
        required=False,
        help_text=_("Xodim qabul qiladigan kunlarni tanlang")
    )
    
    class Meta:
        model = Employee
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Mavjud ma'lumotlarni yuklash
            self.fields['admission_days_choices'].initial = self.instance.get_admission_days_list()
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Tanlangan kunlarni saqlash
        selected_days = self.cleaned_data.get('admission_days_choices', [])
        instance.set_admission_days_list(selected_days)
        if commit:
            instance.save()
        return instance
