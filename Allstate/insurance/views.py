from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, CustomerAddForm
from insurance.models import AddCustomer

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f"User registered successfully.")
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'insurance/register.html', {'form':form})

def home(request):
	user = request.user
	context = {}
	if user.is_authenticated:
		print("Login successful")
	else:
		return redirect('login')
	return render(request, 'insurance/home.html', context)	


def add_customer(request):
	if request.method == 'POST':
		form = CustomerAddForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f"Customer added successfully.")
			return redirect('home')
		else:
			return render(request, 'insurance/add_customer.html', {'form':form})		
	else:
		form = CustomerAddForm()
	return render(request, 'insurance/add_customer.html', {'form':form})

def view_customers(request):
	return render(request, 'insurance/home.html', {'customers':AddCustomer.objects.all()})

def update_customer(request, name):
	if request.method == 'GET':
		obj = AddCustomer.objects.get(name=name)
		form = CustomerAddForm(instance=obj)
		form.fields['name'].disabled = True
		form.fields['insurance_type'].disabled = True
		return render(request, 'insurance/add_customer.html', {'form':form,'update':True,
																'name':name})
	else:
		data = request.POST
		AddCustomer.objects.filter(name=name).update(age=data['age'], salary=data['salary']
													,company=data['company'])
		messages.success(request, f"Customer updated successfully.")
		return render(request, 'insurance/home.html', {'customers':AddCustomer.objects.all()})


def delete_customer(request, cname):
	AddCustomer.objects.filter(name=cname).delete()
	messages.success(request, "Customer deleted successfully!")
	return render(request, 'insurance/home.html', {'customers':AddCustomer.objects.all()})
