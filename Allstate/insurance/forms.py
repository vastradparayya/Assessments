from django import forms
from django.contrib.auth.models import User
from .models import AddCustomer
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	 username = forms.CharField(label='First Name(Username)', max_length=150)
	 surname = forms.CharField(label='Last Name', required=False, max_length=150)
	 email = forms.EmailField()


	 class Meta:
	 	model = User
	 	fields = ['username','surname','email','password1','password2']
	 	# fields = '__all__'


class CustomerAddForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=150)
	age = forms.IntegerField(label='Age')
	salary = forms.IntegerField(label='Salary')
	company = forms.CharField(label='Company', max_length=300)
	insurance_type = forms.CharField(max_length=150,
		widget=forms.Select(choices=[
			('Basic: $10/month premium + Tax', 'Basic: $10/month premium + Tax'),
			('Gold: $15/month premium + Tax', 'Gold: $15/month premium + Tax'),
			('Platinum: $20/month premium + Tax', 'Platinum: $20/month premium + Tax'),
			]))

	class Meta:
		model = AddCustomer
		fields = '__all__'