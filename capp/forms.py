from django import forms
from capp.models import Employee

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'
		