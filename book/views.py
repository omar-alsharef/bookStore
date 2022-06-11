from django.shortcuts import redirect, render

from book.models import Book
from .forms import BookForm
# Create your views here.
def Index(request):
     return render(request, 'book/Index.html', {'list':Book.objects.all()})


def Create(request):
    form = BookForm(request.POST)
    
    if(request.method =='POST'):
         if(form.is_valid):
              form.save()
              return redirect('book:Index')
    else:
         return render(request,'book/Create.html', {'ff':BookForm})


def Details(request, book_id):
    bok = Book.objects.get(pk=book_id)
    return render(request,'book/Details.html', {'ff':bok})


def Edit(request, book_id):
    bok = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None,instance=bok)
    if(request.method =='POST'):
         if(form.is_valid):
          form.save()    
          return redirect('book:Index')
    else:
         return render(request,'book/Edit.html',{'ff':form})


def Delete(request, book_id):
     bok =Book.objects.get(pk=book_id)
     if(request.method =='POST'):
          bok.delete()
          return redirect('book:Index')
          
     else:
         return render(request,'book/Delete.html',{'ff':bok})     