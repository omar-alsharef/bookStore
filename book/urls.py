from . import views
from django.urls import path
app_name = 'book'
urlpatterns = [

    path('', views.Index, name='Index'),
    path('Create', views.Create, name='Create'),
    path('Details/<book_id>', views.Details, name='Details'),
    path('Edit/<book_id>', views.Edit, name='Edit'),
    path('Delete/<book_id>', views.Delete, name='Delete'),

]
