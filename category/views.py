from django.shortcuts import redirect, render

from category.forms import CategoryForm
from .models import Category
# Create your views here.
def Index(request):
     return render(request, 'category/Index.html', {'list':Category.objects.all()})


def Create(request):
    form = CategoryForm(request.POST)
    if(request.method == 'POST'):
         if(form.is_valid):
              form.save()
              return redirect('category:Index')
    else:
        return render(request, 'category/Create.html', {'ff':form})          


def Edit(request,category_id):
     cat = Category.objects.get(pk=category_id)
     form =CategoryForm(request.POST or None,instance=cat)
     if(request.method =='POST'):
          if(form.is_valid):
               form.save()
               return redirect('category:Index')
     else:
          return render(request, 'category/Edit.html', {'ff':form})

def Delete(request,category_id):
     cat = Category.objects.get(pk=category_id)
     if(request.method =='POST'):
          cat.delete()
          return redirect('category:Index')
     else:
          return render(request,'category/Delete.html',{'cat':cat})
