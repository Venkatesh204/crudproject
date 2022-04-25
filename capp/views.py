from django.shortcuts import render,redirect
from capp.models import Employee
from capp.forms import EmployeeForm

# Create your views here.
 
def read_view(request):
	employees = Employee.objects.all()
	return render(request,'capp/home.html',{'employees':employees})

def insert_view(request):
	form=EmployeeForm()
	if request.method=="POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')
	return render(request,'capp/insert.html',{'form':form})

def delete_view(request,id):
	employee = Employee.objects.get(id=id)
	employee.delete()
	return redirect('/home')

def update_view(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST,instance=employee) #instance=employee means replacing existing record
		if form.is_valid():
			form.save()
		return redirect('/home') #redirecting to results page like sample.html
	return render(request,'capp/update.html',{'employee':employee})

    