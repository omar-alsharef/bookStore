from django.shortcuts import redirect, render
from trans.models import Trans
from .forms import TransForm
# Create your views here.
def Index(request):
     return render(request, 'trans/Index.html', {'list':Trans.objects.all()})


def Create(request):
    form = TransForm(request.POST)
    if(request.method =='POST'):
         if(form.is_valid):
              form.save()
              return redirect('trans:Index')
    else:
          return render(request,'trans/Create.html', {'ff':TransForm})


def Details(request, trans_id):
    bor = Trans.objects.get(pk=trans_id)
    return render(request,'trans/Details.html', {'ff':bor})


def Edit(request, trans_id):
    bor = Trans.objects.get(pk=trans_id)
    form = TransForm(request.POST or None,instance=bor)
    if(request.method =='POST'):
         if(form.is_valid):
          form.save()    
          return redirect('trans:Index')
    else:
         return render(request,'trans/Edit.html',{'ff':form})


def Delete(request, trans_id):
     bor =Trans.objects.get(pk=trans_id)
     if(request.method =='POST'):
          bor.delete()
          return redirect('trans:Index')
          
     else:
         return render(request,'trans/Delete.html',{'ff':bor})
