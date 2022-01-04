from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name='home' ),
    path('/home/site/wwwroot/static', admin.site.urls)
    

]