from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError

from .models import Attendance


class AttendanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_errors = defaultdict(list)

    class Meta:
        fields = [
            'name', 'iam', 'email', 'phone_number', 'condo_size',
            'number_condos', 'solution',
        ]
        model = Attendance
    
    def clean_iam(self):
        iam = self.cleaned_data.get('iam')

        if iam == 'S':
            self.my_errors['iam'].append("'Eu sou' é um campo obrigatório")
        
        return iam
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if len(phone_number) < 16:
            self.my_errors['phone_number'].append("Este campo deve ter no mínimo 16 caracteres.")

        return phone_number
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if '@' not in email:
            self.my_errors['email'].append('Endereço de e-mail inválido')
        
        return email
    
    def clean_solution(self):
        solution = self.cleaned_data.get('solution')

        if solution == 'S':
            self.my_errors['solution'].append('Solução é um campo obrigatório')
        
        return solution
    
    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        if self.my_errors:
            raise ValidationError(self.my_errors)

        return super_clean

    