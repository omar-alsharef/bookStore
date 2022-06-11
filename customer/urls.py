from . import views
from django.urls import path
app_name = 'customer'
urlpatterns = [

    path('', views.Index, name='Index'),
    path('Create', views.Create, name='Create'),
    path('Details/<customer_id>', views.Details, name='Details'),
    path('Edit/<customer_id>', views.Edit, name='Edit'),
    path('Delete/<customer_id>', views.Delete, name='Delete'),

]
