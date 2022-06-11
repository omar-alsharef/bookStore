from . import views
from django.urls import path
app_name = 'user'
urlpatterns = [

    path('', views.Login, name='Login'),
    path('Home', views.Home, name='Home'),
    path('Index', views.Index, name='Index'),
    path('Create', views.Create, name='Create'),
    path('Edit/<user_id>', views.Edit, name='Edit'),
    path('Delete/<user_id>', views.Delete, name='Delete'),
    path('Logout', views.Logout, name='Logout'),
]