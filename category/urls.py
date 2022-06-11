from . import views
from django.urls import path
app_name='category'
urlpatterns = [

    path('', views.Index, name='Index'),
    path('create', views.Create, name='Create'),
    path('edit/<category_id>', views.Edit, name='Edit'),
    path('delete/<category_id>', views.Delete, name='Delete'),
] 
