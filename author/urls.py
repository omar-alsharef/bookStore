from . import views
from django.urls import path
app_name = 'author'
urlpatterns=[
    path('', views.Index, name='Index'),
    path('Create', views.Create, name='Create'),
    path('Details/<author_id>', views.Details, name='Details'),
    path('Edit/<author_id>', views.Edit, name='Edit'),
    path('Delete/<author_id>', views.Delete, name='Delete'),
]