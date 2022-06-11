from django.shortcuts import redirect, render

from user.models import User
from user.forms import UserForm
# Create your views here.


def Login(request):
    if(request.method == 'POST'):

        username = request.POST.get('userName')
        password = request.POST.get('password')
        result=User.objects.filter(userName=username,password=password).count()
        
       
        if(result==0):
           return render(request, 'user/Login.html', {"Result":'Invalid username or password'})
        else:
            
            request.session['userName'] = username
            return redirect('user:Home')
            
    else:
        return render(request, 'user/Login.html')


def Home(request):
    return render(request, 'user/Home.html')


def Index(request):
     
     return render(request, 'user/Index.html',{'list':User.objects.all()})


def Create(request):
     if (request.method == 'POST'):
          form = UserForm(request.POST)
          form.save()
          return redirect('user:Index')

     else:
          return render(request, 'user/Create.html', {'ff': UserForm})     


def Edit(request, user_id):
     nat = User.objects.get(pk= user_id)
     form =  UserForm(request.POST or None, instance=nat)
     if(request.method =='POST'):
         if(form.is_valid):
              form.save() 
              return redirect('user:Index')
     else:
          return render(request, 'user/Edit.html', {'ff':form})
     

def Delete (request,  user_id):
     nat =  User.objects.get(pk= user_id)
     if(request.method == 'POST'):
          nat.delete()
          return redirect('user:Index')

     else:
          return render(request, 'user/Delete.html', {'nat': nat})    


def Logout (request):          
    try:
        del request.session['userName']
    except KeyError:
        pass

    return redirect('user:Login')