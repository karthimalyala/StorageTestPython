from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('/home/site/wwwroot/static',views.home,name='home' ),
 
    

]