from django.urls import path
from . import views
app_name = 'nationality'
urlpatterns = [
    path('', views.Index , name='Index'),
    path('Create', views.Create, name='Create'),
    path('Edit/<nationality_id>', views.Edit , name='Edit'),
    path('Delete/<nationality_id>',views.Delete,name='Delete'),
    
]