from . import views
from django.urls import path
app_name = 'trans'
urlpatterns = [

    path('', views.Index, name='Index'),
    path('Create', views.Create, name='Create'),
    path('Details/<trans_id>', views.Details, name='Details'),
    path('Edit/<trans_id>', views.Edit, name='Edit'),
    path('Delete/<trans_id>', views.Delete, name='Delete'),

]