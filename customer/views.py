from django.shortcuts import redirect, render
from customer.models import Customer
from .forms import CustomerForm
# Create your views here.
def Index(request):
     return render(request, 'customer/Index.html', {'list':Customer.objects.all()})


def Create(request):
    form = CustomerForm(request.POST)
    if(request.method =='POST'):
         if(form.is_valid):
              form.save()
              return redirect('customer:Index')
    else:
         return render(request,'customer/Create.html', {'ff':CustomerForm})


def Details(request, customer_id):
    mer = Customer.objects.get(pk=customer_id)
    return render(request,'customer/Details.html', {'ff':mer})


def Edit(request, customer_id):
    mer = Customer.objects.get(pk=customer_id)
    form = CustomerForm(request.POST or None,instance=mer)
    if(request.method =='POST'):
         if(form.is_valid):
          form.save()    
          return redirect('customer:Index')
    else:
         return render(request,'customer/Edit.html',{'ff':form})


def Delete(request, customer_id):
     mer =Customer.objects.get(pk=customer_id)
     if(request.method =='POST'):
          mer.delete()
          return redirect('customer:Index')
          
     else:
         return render(request,'customer/Delete.html',{'ff':mer})
