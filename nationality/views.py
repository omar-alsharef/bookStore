from django.shortcuts import redirect, render
from nationality.forms import NationalityForm

from nationality.models import Nationality

def Index(request):
     
     return render(request, 'nationality/Index.html',{'list':Nationality.objects.all()})


def Create(request):
     if (request.method == 'POST'):
          form = NationalityForm(request.POST)
          form.save()
          return redirect('nationality:Index')

     else:
          return render(request, 'nationality/Create.html', {'ff': NationalityForm})     



def Edit(request,nationality_id):
     nat = Nationality.objects.get(pk=nationality_id)
     form = NationalityForm(request.POST or None, instance=nat)
     if(request.method =='POST'):
         if(form.is_valid):
              form.save() 
              return redirect('nationality:Index')
     else:
          return render(request, 'nationality/Edit.html', {'ff':form})
     

def Delete (request, nationality_id):
     nat = Nationality.objects.get(pk=nationality_id)
     if(request.method == 'POST'):
          nat.delete()
          return redirect('nationality:Index')

     else:
          return render(request, 'nationality/Delete.html', {'nat': nat})     


def Search(request):
    if(request.method == 'POST'):
       searched = request.POST['SearchText']
       nats = Nationality.objects.filter(nationalityName__contains=searched)
       return render(request, 'nationality/search.html', {'nats': nats, 'searched': searched})
    else:
      return  render(request,'nationality/search.html')