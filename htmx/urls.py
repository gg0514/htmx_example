from django.urls import path
from . import views


urlpatterns = [
    path('hello', views.hello, name='hello'),                           
    path('basic', views.basic, name='basic'),     

    path('get-user-data', views.get_user_data, name='get_user_data'),     
    path('dummy', views.dummy, name='dummy'),     
] 
