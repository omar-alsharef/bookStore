from django.shortcuts import redirect, render

from author.models import Author
from .forms import AuthorForm

# Create your views here.


def Index(request):
    return render(request, 'author/Index.html', {'list': Author.objects.all()})


def Create(request):
    if(request.method=='POST'):
        atr = AuthorForm(request.POST)
        if(atr.is_valid):
             atr.save()
             return redirect('author:Index')
    else:
          return render(request,'author/Create.html',{'ff':AuthorForm})         


def Details(request,author_id):
    atr = Author.objects.get(pk=author_id)

    return render(request,'author/Details.html',{'ff':atr})    


def Edit(request, author_id):
    atr = Author.objects.get(pk=author_id)
    form = AuthorForm(request.POST or None,instance=atr)
    if(request.method =='POST'):
        if(form.is_valid):
            form.save()
            return redirect('author:Index')
    else:
        return render(request,'author/Edit.html', {'ff':form})         


def Delete(request, author_id):
    atr = Author.objects.get(pk=author_id)
    if(request.method =='POST'):
        atr.delete()
        return redirect('author:Index')
    else:
        return render(request,'author/Delete.html', {'ff':atr})








